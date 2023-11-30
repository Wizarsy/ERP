import smtplib
from email.mime.multipart import MIMEMultipart

from src.config import CONFIG


def sendEmail(target: str, subject: str, content: any) -> None:
  server = smtplib.SMTP(**CONFIG["email"]["SMTP"])
  server.starttls()
  server.login(**CONFIG["email"]["LOGIN"])
  server.sendmail(CONFIG["email"]["LOGIN"]["user"], {target}, f"Subject: {subject}\n\n{content}")
  server.quit()
