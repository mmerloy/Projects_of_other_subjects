import os
import email
from imaplib import IMAP4_SSL
from time import sleep
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

EMAIL_LOGIN = os.getenv('EMAIL_LOGIN')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
IMAP_HOST = os.getenv('IMAP_HOST')
IMAP_PORT = os.getenv('IMAP_PORT')
SMTP_HOST = os.getenv('SMTP_HOST')
SMTP_PORT = os.getenv('SMTP_PORT')
PERIOD_CHECK = int(os.getenv('PERIOD_CHECK'))

with IMAP4_SSL(IMAP_HOST, int(IMAP_PORT)) as IMAP4:
    rc, resp = IMAP4.login(EMAIL_LOGIN, EMAIL_PASSWORD)
    while True:
        IMAP4.select()  # Выбор почтового ящика
        status, msgnums = IMAP4.search(None, '(From "freem598@gmail.com")', '(Unseen)')
        messages = msgnums[0].split()
        for num in messages:
            typ, data = IMAP4.fetch(num, '(RFC822)')
            text_mail = data[0][1]
            email_message = email.message_from_bytes(text_mail)
            body = email_message.get_payload()[0].get_payload(decode=True).decode('utf-8')
            subject = int(email_message['ID'])
            print(subject)
            with open("test_file.txt", "r") as f:
                IDs = [int(line) for line in f]
            if subject in IDs:
                log = open("success_request.log", "a")
            else:
                log = open("error_request.log", "a")
            log.write("%s: %s\n" % (subject, body))
            log.close()
        sleep(PERIOD_CHECK)
