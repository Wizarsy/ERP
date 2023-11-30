import time

from psycopg.errors import UniqueViolation
from psycopg.rows import dict_row
from psycopg_pool import ConnectionPool
from src.config import CONFIG

db = ConnectionPool(kwargs = {**CONFIG["db"], "row_factory": dict_row, "autocommit": True})

with db.connection() as dq:
  print(dq.execute("SELECT * FROM users_account").fetchall())