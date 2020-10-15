import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 25)

server.ehlo()

with open('/home/aarmik/Documents/secure/mail.txt', 'r' ) as f:
    password = f.read()

server.login('eisd345@gmail.com', password)

msg = MIMEMultipart()
msg['From'] = 'eisd'
msg['To'] = ' xlybljvrcwxummqjkb@niwghx.online'
msg['Subject'] = 'Just a Test'

with open('message.txt', 'r') as m:
    message = m.read()

msg.attach(MIMEText(message, 'plain'))