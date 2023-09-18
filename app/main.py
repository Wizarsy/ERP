import src.db as db
from src.app import app


def main():
  db.init()
  app.run(host = "0.0.0.0")
  
if __name__ == "__main__":
 main()