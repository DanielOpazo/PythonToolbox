import smtplib
from email.mime.text import MIMEText

message = "Test Email please ignore"

msg = MIMEText(message)
msg['Subject'] = 'Raspberry Pi Python test'
msg['From'] = 'daniel\'s raspberry pi'
#msg['To'] = 'samson.truong@gmail.com'
msg['To'] = 'daniel.opazo.baer@gmail.com'

#s = smtplib.SMTP('smtp.gmail.com', 465)
s = smtplib.SMTP('localhost')
#s.login('daniel.opazo.baer@gmail.com', 'insert password')
s.login('pi', 'raspberry')
s.sendmail(msg['From'], msg['To'], msg.as_string())
s.quit()
