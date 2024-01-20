import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import config

# Set your email and password
email_address = config.SENDER_EMAIL

# create app password from security settings
# At frist enable 2 step verification
# Then in the 2 step verification page in the button find app password section
app_password = config.APP_PASSWORD

# Set the recipient email address
recipient_email = "takiuddinahmed@gmail.com"

# Create the MIME object
message = MIMEMultipart()
message['From'] = email_address
message['To'] = recipient_email
message['Subject'] = "Test Email"

# Add the email body
body = "This is test email from python"
message.attach(MIMEText(body, 'plain'))

# Set up the SMTP server
smtp_server = "smtp.gmail.com"
smtp_port = 465  # Use 587 if you're using TLS instead of SSL

# Establish a secure connection to the SMTP server
context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
    # Log in to your email account
    server.login(email_address, app_password)

    # Send the email
    server.sendmail(email_address, recipient_email, message.as_string())

print("Email sent successfully!")
