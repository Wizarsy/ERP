import datetime
import os

CONFIG = {
  "db": {
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASS"),
    "dbname": os.getenv("DB_NAME"),
    "host": os.getenv("DB_HOST")
  },
  
  "flask": {
    "DEBUG": os.getenv("FLASK_DEBUG"),
    "SECRET_KEY": os.getenv("FLASK_SECRET_KEY"),
    "SESSION_COOKIE_SECURE": os.getenv("FLASK_SESSION_COOKIE_SECURE"),
    "SESSION_COOKIE_NAME": "flaskSession",
    "PERMANENT_SESSION_LIFETIME": datetime.timedelta(days = 1),
    "SESSION_REFRESH_EACH_REQUEST": False
  }
}