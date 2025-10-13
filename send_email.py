import smtplib, ssl
from getpass import getpass
smtp_server= 'smpt.gmail.com'
port =465
sender_email = ''
receiver_email= ''
password = getpass(prompt='enter your pass')
massage = ' hi this my pm'
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server,port,context=context) as server:
    server.login(sender_email,password)
    server.sendmail(sender_email,receiver_email,massage)
