# Database code for the DB Forum, full solution!

import sqlite3, bleach

DBNAME = "forum"

def get_posts():
  db = sqlite3.connect(database=DBNAME)
  c = db.cursor()
  c.execute("""select content, time from posts order by time desc;""")
  posts = c.fetchall()
  db.close()
  return posts

def add_post(contents):
  db = sqlite3.connect(database=DBNAME)
  c = db.cursor()
  c.execute("""insert into posts (content) values (?);""",(bleach.clean(contents),))
  db.commit()
  db.close()

def init_post():
    db = sqlite3.connect(database=DBNAME)
    c = db.cursor()
    #c.execute("""DROP TABLE posts;""")

    sql_command = """
    CREATE TABLE posts ( content TEXT,
                     time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                     id SERIAL );"""

    c.execute(sql_command)
    db.close()