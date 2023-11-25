from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import logging
import time
import json

from dotenv import load_dotenv
from pandas import DataFrame

load_dotenv()


class Mail:
    # onfig = json.loads(open(".credentials.json").read())
    subject = "Free Epic Games Reminder"
    message = "You weekly Epic Games Reminder Is Here;"
    # email = MIMEMultipart("alternative")
    smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)

    def __init__(self, credentials_path: str) -> None:
        self.config = json.loads(open(credentials_path).read())

        logging.debug(
            f"sender: {self.config['EMAIL']}, subject: {self.subject}, message: {self.message}"
        )

    def send(self, data: DataFrame):
        self.smtp.starttls()
        self.smtp.login(self.config["EMAIL"], self.config["PASSWORD"])
        self.email = self.create_html_body(data)

        for rec in self.config["RECEIVERS"]:
            self.email["From"] = self.config["EMAIL"]
            self.email["To"] = rec
            self.email["Subject"] = self.subject

            logging.info(f"mail sent, rec: {rec}")
            self.smtp.sendmail(self.config["EMAIL"], rec, self.email.as_string())
            time.sleep(2)
        self.smtp.quit()

    def create_html_body(self, data: DataFrame):
        body = f"""
            <html>
              <body>
                <p>Hi!, How are you?<br>
                   You weekly Epic Games Reminder Is Here
                {data.to_html(na_rep = "", index = False).replace("<th>","<th style = 'background-color: gray; color: white; text-align: center'>").replace("<td>","<td style = 'text-align: start; padding: 10px;'>")}
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
