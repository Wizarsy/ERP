import asyncio

import src.db as db
from src.app import app


async def main():
  await db.init()
  app.run(host = "0.0.0.0", debug = True)
  
if __name__ == "__main__":
  asyncio.run(main())