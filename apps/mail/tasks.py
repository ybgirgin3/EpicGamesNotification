import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Optional

from tabulate import tabulate


class Mail:
    sender = "epicfreegamesreminder@outlook.com"
    subject = "Free Epic Games Reminder"
    message = "You weekly Epic Games Reminder Is Here;"
    # email = MIMEMultipart("alternative")
    smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)

    logging.debug(f'sender: {sender}, subject: {subject}, message: {message}')

    def __init__(self, rec: Optional[list] = None) -> None:
        self.recipient: str = "ybgirgin3@gmail.com"  # senders will be list reading by db

    def send(self):
        self.email = self.create_html_body()
        self.email["From"] = self.sender
        self.email["To"] = self.recipient
        self.email["Subject"] = self.subject
        # self.email.attach(self.create_html_body())

        self.smtp.starttls()
        self.smtp.login(self.sender, "/P_VK5sH!SCi4#f")
        self.smtp.sendmail(self.sender, self.recipient, self.email.as_string())
        self.smtp.quit()

    def create_html_body(self):
        body = """
            <html>
              <body>
                <p>Hi,<br>
                   How are you?<br>
                   "You weekly Epic Games Reminder Is Here
                   <a href="http://ybgirgin3.github.io">Bekocan personal site</a> 
                {table}
                </p>
              </body>
            </html>
            """
        logging.debug('body of the mail {}'.format(body))
        import csv
        with open('../freegames.csv') as inpf:
            data = list(csv.reader(inpf))
        html = body.format(table=tabulate(data, headers="firstrow", tablefmt="html"))

        return MIMEMultipart(
            "alternative", None, [MIMEText(html, 'html')])
