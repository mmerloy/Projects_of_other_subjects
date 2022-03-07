import socket

HOST = '127.0.0.1'
PORT = 9080
while True:
    username = "freem598@gmail.com"
    text_message = input("Введите , пожалуйста , ваше сообщение: ")
    message = username + "|" + text_message
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', PORT))
        s.sendall(message.encode())
        data = s.recv(2048)
        if data.decode() == "OK":
            break
    print('Received', repr(data))
s.close()

