import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Optional
import csv
import pandas as pd


class Mail:
    sender = ("epicfreegamesreminder@outlook.com", "/P_VK5sH!SCi4#f")
    subject = "Free Epic Games Reminder"
    message = "You weekly Epic Games Reminder Is Here;"
    # email = MIMEMultipart("alternative")
    smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)

    logging.debug(f'sender: {sender}, subject: {subject}, message: {message}')


    def __init__(self, rec: Optional[list] = None, data: pd.DataFrame = "") -> None:
        self.recipient: str = "ybgirgin3@gmail.com"  # senders will be list reading by db
        self.data: str = data

    def send(self):
        self.email = self.create_html_body()
        self.email["From"] = self.sender[0]
        self.email["To"] = self.recipient
        self.email["Subject"] = self.subject
        # self.email.attach(self.create_html_body())

        self.smtp.starttls()
        self.smtp.login(self.sender[0], self.sender[1])
        self.smtp.sendmail(self.sender[0], self.recipient, self.email.as_string())
        self.smtp.quit()

    def create_html_body(self):
        body = f"""
            <html>
              <body>
                <p>Hi,<br>
                   How are you?<br>
                   You weekly Epic Games Reminder Is Here
                   <a href="http://ybgirgin3.github.io">Bekocan personal site</a> 
                {self.data.to_html()}
                <br>
                Find an issue? Let us know
                <a href='https://github.com/ybgirgin3/EpicGamesNotification'>https://github.com/ybgirgin3/EpicGamesNotification</a>
                </p>
              </body>
            </html>
            """
        logging.debug('body of the mail {}'.format(body))

        return MIMEMultipart(
            "alternative", None, [MIMEText(body, 'html')])
