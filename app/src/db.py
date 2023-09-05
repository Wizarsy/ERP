import psycopg2 as pg
import time
import asyncio
from src.config import CONFIG

async def init():
  print(f"Trying to connect to the DB...")
  while True:
    try:
      db = pg.connect(**CONFIG["db"])
      print(f"Connected to the DB.")
      break
    except Exception:
      time.sleep(5)