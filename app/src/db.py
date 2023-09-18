import time

from psycopg.rows import dict_row
from psycopg_pool import ConnectionPool, errors
from src.config import CONFIG

db = ConnectionPool(open = False, kwargs = {**CONFIG["db"], "row_factory": dict_row, "autocommit": True})

def init():
  print(f"Trying to connect to the DB...")
  while True:
    try:
      db.open()
      with db.connection() as conn:
        conn.execute(
          """CREATE TABLE IF NOT EXISTS users (
                                                id SERIAL PRIMARY KEY, 
                                                username TEXT NOT NULL, 
                                                email TEXT NOT NULL, 
                                                passwh TEXT NOT NULL);
                                                """)
        conn.execute("INSERT INTO users (username, email, passwh) VALUES (%s, %s, %s)", 
                     ("wizarsy", "email@email.com", "pbkdf2:sha256:600000$YEV8SofkYUB65EY8$5338ff8cb37825355a5b4f603995036cdcb1ee82be08d48361739e029fe90bfc"))
      print("Connected to the DB.")
      break
    except errors.PoolTimeout:
      print("Connection error, trying again...")
      db.close()
      time.sleep(5)