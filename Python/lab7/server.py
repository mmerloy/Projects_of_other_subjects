import os
import socket
import random
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

HOST = '127.0.0.1'
PORT = 9080
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
EMAIL_LOGIN = os.getenv('EMAIL_LOGIN')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
IMAP_HOST = os.getenv('IMAP_HOST')
IMAP_PORT = os.getenv('IMAP_PORT')
SMTP_HOST = os.getenv('SMTP_HOST')
SMTP_PORT = os.getenv('SMTP_PORT')
PERIOD_CHECK = os.getenv('PERIOD_CHECK')


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('', PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Подключено к ', addr)
        data = conn.recv(2048)
        while True:
            user_email, text = data.decode().split('|')
            print("Email: " + user_email + "\nСообщение: " + text)
            if ".com" and "@" not in user_email:
                conn.sendall(b'Error')
            else:
                conn.sendall(b'OK')
                ID = random.randint(1, 10000)  # создали уникальный ID (защищенный)
                with open("test_file.txt", "a") as test_file:
                    test_file.write(str(ID) + '\n')
                with SMTP("smtp.gmail.com:587") as smpt:
                    msg = MIMEMultipart()
                    msg['ID'] = str(ID)
                    msg['From'] = EMAIL_LOGIN
                    msg['To'] = user_email
                    msg.attach(MIMEText(text, 'plain'))

                    msg2 = MIMEMultipart()
                    msg2['ID'] = str(ID)
                    msg2['From'] = EMAIL_LOGIN
                    msg2['To'] = EMAIL_LOGIN
                    msg2.attach(MIMEText(text, 'plain'))

                    smpt.starttls()  # переводим SMTP-соединение в режим TLS
                    smpt.login(EMAIL_LOGIN, EMAIL_PASSWORD)  # Входим на SMTP-сервер, требующий проверки подлинности.
                    smpt.sendmail(EMAIL_LOGIN, user_email, msg.as_string())
                    smpt.sendmail(EMAIL_LOGIN, EMAIL_LOGIN, msg2.as_string())
                break
    s.close()


