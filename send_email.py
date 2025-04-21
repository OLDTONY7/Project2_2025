import smtplib
from email.message import EmailMessage

#Set the sender email and password and recipient emaiç
from_email_addr ="tonyold7@outlook.com"
from_email_pass ="jvzinwjdwiwgwksx"
to_email_addr ="tonyold7@163.com"

# Create a message object
msg = EmailMessage()

# Set the email body
body ="Hello from Raspberry Pi"
msg.set_content(body)

msg['From'] = from_email_addr
msg['To'] = to_email_addr

msg['Subject'] = 'TEST EMAIL'

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login(from_email_addr,from_email_pass)

server_send_message(msg)

print('Email sent')

server.quit()
