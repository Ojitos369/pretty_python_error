import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

EMAIL_SETTINGS = {
    'smtp_server': os.environ.get('SMTP_SERVER'),
    'port': int(os.environ.get('SMTP_PORT')),
    'sender': os.environ.get('SMTP_SENDER'),
    'receiver': os.environ.get('SMTP_RECEIVER', 'ojitos369@gmail.com'),
    'password': os.environ.get('SMTP_PASSWORD')
}


class Email:
    def __init__(self, message):
        self.msg = MIMEMultipart()
        self.server = smtplib.SMTP_SSL(EMAIL_SETTINGS['smtp_server'], EMAIL_SETTINGS['port'])
        self.server.login(EMAIL_SETTINGS['sender'], EMAIL_SETTINGS['password'])
        self.message = message

    def send(self):
        self.msg['From'] = self.sender
        self.msg['Subject'] = self.subject
        self.msg['To'] = self.receiver
        self.msg.attach(MIMEText(self.message, 'plain'))
        self.server.sendmail(self.msg['From'], self.msg['To'], self.msg.as_string())
        self.server.quit()


class ErrorEmail(Email):
    sender = EMAIL_SETTINGS['sender']
    subject = 'ERROR EN <NOMBRE DEL PROYECYO>'
    receiver = EMAIL_SETTINGS['receiver']

