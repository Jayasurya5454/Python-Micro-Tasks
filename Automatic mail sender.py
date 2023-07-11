import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, message):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    email_message = MIMEMultipart()
    email_message["From"] = sender_email
    email_message["To"] = recipient_email
    email_message["Subject"] = subject
    email_message.attach(MIMEText(message, "plain"))
    server.send_message(email_message)
    server.quit()


sender_email = "Sender_email@gmail.com"
sender_password = "Sender_password"
recipient_email = "recipient_email@example.com"
subject = "Automated Email"
message = "Hello, this is an automated email sent using Python!"
send_email(sender_email, sender_password, recipient_email, subject, message)
