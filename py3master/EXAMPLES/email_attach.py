#!/usr/bin/env python
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

DEBUG = False # default, but just in case
# DEBUGGING output for an image will overwhelm most
#  IDEs' output buffers

SMTP_SERVER = "smtpcorp.com"
SMTP_PORT = 2525
SMTP_USER = 'jstrickpython'
SMTP_PWD = 'python(monty)'

SENDER = 'jstrick@mindspring.com'
RECIPIENTS = ['jstrickler@gmail.com']

def main():
    smtp_server = create_smtp_server()
    msg = create_message(
        'Here is your attachment',
        'Testing email attachments from python class.',
    )
    add_text_attachment('../DATA/parrot.txt', msg)
    add_image_attachment('../DATA/felix_auto.jpeg', msg)
    send_message(smtp_server, msg)


def create_message(subject, body):
    msg = MIMEMultipart(body)
    msg['Subject'] = subject

    return msg

def add_text_attachment(file_name, message):
    with open(file_name) as file_in:
        attachment_data = file_in.read()

    short_name = os.path.basename(file_name)
    attachment = MIMEText(attachment_data)
    attachment.add_header(
        'Content-Disposition', 'attachment', filename=short_name
    )

    message.attach(attachment)

def add_image_attachment(file_name, message):
    with open(file_name, 'rb') as file_in:
        attachment_data = file_in.read()

    short_name = os.path.basename(file_name)
    attachment = MIMEImage(attachment_data)
    attachment.add_header(
        'Content-Disposition', 'attachment', filename=short_name
    )

    message.attach(attachment)


def create_smtp_server():
    smtpserver = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtpserver.login(SMTP_USER, SMTP_PWD)
    smtpserver.set_debuglevel(DEBUG) # show communication with the server

    return smtpserver

def send_message(server, message):
    try:
        server.sendmail(
            SENDER,
            RECIPIENTS,
            message.as_string()
        )
    finally:
        server.quit()

if __name__ == '__main__':
    main()
