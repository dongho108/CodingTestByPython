#-*-coding:utf-8-*-

import smtplib
from email.mime.text import MIMEText

pop_server = "pop.naver.com"
smtp_server = "smtp.naver.com"
smtp_port = 465 # SSL 필요
my_id = "dongho108"
my_password = '@rlaehdgh8572'

smtp = smtplib.SMTP_SSL(smtp_server, smtp_port)
smtp.ehlo()
smtp.login(my_id, my_password)

msg = MIMEText('안녕하세요')
msg['Subject'] = '테스트 메일'
msg['To'] = "dongho108@naver.com"
smtp.sendmail("dongho108@naver.com", "dongho108@naver.com", msg.as_string())
smtp.quit()