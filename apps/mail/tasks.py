import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Optional
import smtplib
import logging
import time
import json

from dotenv import load_dotenv

load_dotenv()


class Mail:
  sender = json.loads(open('.credentials.json').read())
  print('sender:', sender)
  subject = "Free Epic Games Reminder"
  message = "You weekly Epic Games Reminder Is Here;"
  # email = MIMEMultipart("alternative")
  smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)

  logging.debug(
    f"sender: {sender['EMAIL']}, subject: {subject}, message: {message}")

  def __init__(
      self,
      rec: Optional[list] = None,
      data: pd.DataFrame = ""
  ) -> None:

    self.data: str = data
    with open('subs.txt') as f:
      self.recipients = [
        i.strip() for i in f.readlines()
        if not i.startswith('#')
      ]

  def send(self):
    self.smtp.starttls()
    self.smtp.login(self.sender['EMAIL'], self.sender['PASSWORD'])
    self.email = self.create_html_body()

    for rec in self.recipients:
      self.email["From"] = self.sender['EMAIL']
      self.email["To"] = rec
      self.email["Subject"] = self.subject

      logging.info(f"mail sent, rec: {rec}")
      self.smtp.sendmail(
        self.sender['EMAIL'],
        rec,
        self.email.as_string())
      time.sleep(2)
    self.smtp.quit()

  def create_html_body(self):
    body = f"""
            <html>
              <body>
                <p>Hi!, How are you?<br>
                   You weekly Epic Games Reminder Is Here
                {self.data.to_html(na_rep = "", index = False).replace("<th>","<th style = 'background-color: gray; color: white; text-align: center'>").replace("<td>","<td style = 'text-align: start; padding: 10px;'>")}
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
