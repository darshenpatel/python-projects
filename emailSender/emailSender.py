import smtplib, ssl
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Any
import credentials

def send_email(to_email: str, subject: str, body: str, image: str | None = None):
    host: str = 'smtp.gmail.com'
    port: int = 587

    context = ssl.create_default_context()

    with smtplib.SMTP(host, port) as server:
        print('Logging in...')
        # server.ehlo()
        server.starttls(context=context)
        # server.ehlo()
        server.login(credentials.EMAIL, credentials.PASSWORD)

        # Prepare the email
        print('Attempting to send the email...')
        message = MIMEMultipart()
        message['From'] = credentials.EMAIL
        message['To'] = to_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # If there is an attachment, attach it to the e-mail
        if image:
            file: MIMEImage = create_attachment(image)
            message.attach(file)

        # Send the email
        server.sendmail(from_addr=credentials.EMAIL, to_addrs=to_email, msg=message.as_string())

        # Success!
        print('Sent!')


def create_attachment(path: str) -> MIMEImage:
    with open(path, 'rb') as image:
        mimeImage = MIMEImage(image.read())
        mimeImage.add_header('Content-Disposition', f'attachment; filename={path}')
        return mimeImage


if __name__ == '__main__':
    send_email(
        to_email='harikishan8397@gmail.com',
        subject='Test Email with a Python Script',
        body='I created a python script that can send emails offline with a local server',
        # image='gmail-logo.png'
    )