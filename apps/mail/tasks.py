import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from typing import Optional


class Mail:
    sender = "epicfreegamesreminder@outlook.com"
    subject = "Free Epic Games Reminder"
    message = "You weekly Epic Games Reminder Is Here;"

    def __init__(self, rec: Optional[list] = None) -> None:
        self.recipient: list = "ybgirgin3@gmail.com" # senders will be list reading by db


    def send(self):
        self.email = MIMEMultipart("alternative")
        self.email["From"] = self.sender
        self.email["To"] = self.recipient
        self.email["Subject"] = self.subject
        #self.email.set_content(self.message)
        self.email.attach(self.create_html_body(data=[]))

        self.smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
        self.smtp.starttls()
        self.smtp.login(self.sender, "/P_VK5sH!SCi4#f")
        self.smtp.sendmail(self.sender, self.recipient, self.email.as_string())
        self.smtp.quit()


    def create_html_body(self, data):
        #self.email.attach(MIMEText("""\
        return MIMEText("""\
            <html>
              <body>
                <p>Hi,<br>
                   How are you?<br>
                   <a href="http://ybgirgin3.github.io">Bekocan personal site</a> 
                </p>
              </body>
            </html>
            """, "html")


