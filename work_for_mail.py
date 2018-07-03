import smtplib
from email.MIMEText import MIMEText
me = 'movchun@gmail.com'
you = 'devops2017dutepam@gmail.com'
text = 'I want final assignment number9 \n Thank you'
subj = 'readme'
server = "smtp.gmail.com"
port = 25
user_name = "movchun@gmail.com"
user_passwd = "N0nPr1vat"

msg = MIMEText(text, "", "utf-8")
msg['Subject'] = subj
msg['From'] = me
msg['To'] = you

s = smtplib.SMTP(server, port)
s.ehlo()
s.starttls()
s.ehlo()
s.login(user_name, user_passwd)
s.sendmail(me, you, msg.as_string())

s.quit
