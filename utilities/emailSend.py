import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class emailSend:

    def sendEmail(receiver_email):
        port = 465  # For SSL
        sender_email = "maxmustermannjob.de@gmail.com"
        password = input("Type your password and press enter: ")

        message = MIMEMultipart("alternative")
        message["Subject"] = "HushHush Recruiter has a code challenge for you!"
        message["From"] = sender_email
        message["To"] = receiver_email

        html = open("emailSend.html")
        part = MIMEText(html.read(), "html")
        message.attach(part)

        # Create a secure SSL context
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())

    sendEmail("maxmustermannjob.de@gmail.com")