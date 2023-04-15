import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Optional

import pandas as pd

import os


class Mail:
  sender = ("epicfreegamesreminder@outlook.com", "/P_VK5sH!SCi4#f")
  subject = "Free Epic Games Reminder"
  message = "You weekly Epic Games Reminder Is Here;"
  # email = MIMEMultipart("alternative")
  smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)

  logging.debug(f"sender: {sender}, subject: {subject}, message: {message}")

  def __init__(
      self,
      rec: Optional[list] = None,
      data: pd.DataFrame = "") -> None:
    # senders will be list reading by db
    self.recipient: str = "ybgirgin3@gmail.com"
    # self.recipient: str = "is.mahmutcankurt@gmail.com"
    self.data: str = data

  def send(self):
    self.email = self.create_html_body()
    self.email["From"] = self.sender[0]
    self.email["To"] = self.recipient
    self.email["Subject"] = self.subject
    # self.email.attach(self.create_html_body())

    if "SEND" in os.environ:
      logging.info("mail sent")
      self.smtp.starttls()
      self.smtp.login(self.sender[0], self.sender[1])
      self.smtp.sendmail(
        self.sender[0],
        self.recipient,
        self.email.as_string())
      self.smtp.quit()

  def create_html_body(self):
    body = f"""
            <html>
              <body>
                <p>Hi,<br>
                   How are you?<br>
                   You weekly Epic Games Reminder Is Here
                {self.data.to_html()}
                <br>
               </p>
              </body>
              <footer>
                Find an issue? Let me know
                <a href='https://github.com/ybgirgin3/EpicGamesNotification'>https://github.com/ybgirgin3/EpicGamesNotification</a>
                <br>
                Contact me <a href="http://ybgirgin3.github.io">Yusuf Berkay Girgin Personal Website</a>
              </footer>
            </html>
            """

    return MIMEMultipart("alternative", None, [MIMEText(body, "html")])
