import datetime
import os

CONFIG = {
  "token_secret_key": os.getenv("TOKEN_SECRET_KEY"),
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
  },
  "email":{
    "SMTP":{
      "host": os.getenv("SMTP_HOST"),
      "port":os.getenv("SMTP_PORT")
    },
    "LOGIN":{
      "user": os.getenv("EMAIL_ACCOUNT"),
      "password": os.getenv("EMAIL_PASSWORD")
    }
  }
}