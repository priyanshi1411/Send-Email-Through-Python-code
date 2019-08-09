import os
import getpass
import smtplib   #simple mail transfer protocol
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
app_data=open('F:\\zeetron.txt','rb').read()  #file name with path
msg=MIMEMultipart()
msg['Subject']='Python test code for document attachment'
msg['From']='xyz@gmail.com'
password=getpass.getpass('Enter password of email:')
msg['To']='abc@gmail.com'
body=MIMEText('python test code successfully sent')
msg.attach(body)
doc=MIMEApplication(app_data,name=os.path.basename('F:\\zeetron.txt'))
msg.attach(doc)
s=smtplib.SMTP('smtp.gmail.com',587)
s.ehlo()
s.starttls()
s.login(msg['From'],password)
s.sendmail(msg['From'],msg['To'],msg.as_string())
s.quit()
print('Email sent successfully')
input()
