import smtplib
from email.mime.text import MIMEText
from email.header import Header

msg = MIMEText('send by python','plain','utf-8')

from_addr = 'cloudyrainyfox@gmail.com'
password = 'drfegznkfedkzshi'

to_addr = ['thanatos9911@gmail.com', 'thanatos666@outlook.jp', 'yutopposub@gmail.com']

smtp_server = 'smtp.gmail.com'

msg['from'] = Header(from_addr)
msg['To'] = Header(','.join(to_addr))
msg['Subject'] = Header('Test')

# for test
print(msg)
print(msg.as_string)

server = smtplib.SMTP_SSL(smtp_server)
server.connect(smtp_server,465)
server.login(from_addr, password)
server.sendmail(from_addr,
to_addr, msg.as_string())
server.quit()