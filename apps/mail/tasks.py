import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import logging
import time
import json

from dotenv import load_dotenv

load_dotenv()


class Mail:
  config = json.loads(open('.credentials.json').read())
  subject = "Free Epic Games Reminder"
  message = "You weekly Epic Games Reminder Is Here;"
  # email = MIMEMultipart("alternative")
  smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)

  logging.debug(
    f"sender: {config['EMAIL']}, subject: {subject}, message: {message}")

  def __init__(
      self,
      data: pd.DataFrame = ""
  ) -> None:

    self.data: str = data

  def send(self):
    self.smtp.starttls()
    self.smtp.login(self.config['EMAIL'], self.config['PASSWORD'])
    self.email = self.create_html_body()

    for rec in self.config['RECEIVERS']:
      self.email["From"] = self.config['EMAIL']
      self.email["To"] = rec
      self.email["Subject"] = self.subject

      logging.info(f"mail sent, rec: {rec}")
      self.smtp.sendmail(
        self.config['EMAIL'],
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
