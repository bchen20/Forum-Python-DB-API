
from flask import Flask, request, redirect, url_for

import sqlite3

from forumdb import init_post,get_posts, add_post


app = Flask(__name__)

# HTML template for the forum page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>Bohong Forum</title>
    <style>
      h1, form { text-align: center; }
      textarea { width: 400px; height: 150px; }
      div.post { border: 1px solid #999;
                 padding: 10px 10px;
                 margin: 10px 20%%; }
      hr.postbound { width: 50%%; }
      em.date { color: #999 }
    </style>
  </head>
  <body>
    <h1>DB Forum</h1>
    <form method=post>
      <div><textarea id="content" name="content"></textarea></div>
      <div><button id="gogo" type="submit">go message</button></div>
    </form>
    <!-- post content will go here -->
%s
  </body>
</html>
'''

# HTML template for an individual comment
POST = '''\
    <div class=post><em class=date>%s</em><br>%s</div>
'''


@app.route('/', methods=['GET'])
def main():
  try:
      post_content = get_posts()
  except sqlite3.OperationalError:
      init_post()
      post_content = get_posts()
  
  posts = "".join(POST % (date, text) for text, date in post_content)
  html = HTML_WRAP % posts
  return html


@app.route('/', methods=['POST'])
def post():
  message = request.form['content']
  add_post(message)
  return redirect(url_for('main'))


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8008)

