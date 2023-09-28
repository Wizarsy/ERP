import time

from psycopg.errors import UniqueViolation
from psycopg.rows import dict_row
from psycopg_pool import ConnectionPool
from src.config import CONFIG

db = ConnectionPool(kwargs = {**CONFIG["db"], "row_factory": dict_row, "autocommit": True})

def init():
  print(f"Trying to connect to the DB...")
  with db.connection() as dq:
    with dq.transaction():
      dq.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"')
      dq.execute(
        """CREATE TABLE IF NOT EXISTS users_account ( 
                                                      id VARCHAR(255) DEFAULT uuid_generate_v4(), 
                                                      username TEXT NOT NULL, 
                                                      email TEXT UNIQUE NOT NULL, 
                                                      passwh TEXT NOT NULL,
                                                      email_confirmed BOOLEAN DEFAULT False,
                                                      PRIMARY KEY(id, email))
                                                      """)
  print("Connected to the DB.")
  
def firstInit():
  with db.connection() as dq:
    with dq.transaction():
      try:
        dq.execute("INSERT INTO users_account (username, email, passwh) VALUES (%s, %s, %s)", ("wizarsy", "filipemadruga@outlook.com", "pbkdf2:sha256:600000$YEV8SofkYUB65EY8$5338ff8cb37825355a5b4f603995036cdcb1ee82be08d48361739e029fe90bfc"))
      except UniqueViolation:
        print("already exist")
  print(dq.execute("SELECT * FROM users_account").fetchall())