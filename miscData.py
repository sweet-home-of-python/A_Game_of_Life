import socket
import time

host = "localhost"
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
while True:
    buf = input()
    s.send(buf.encode('utf8'))
    result = s.recv(1024)
    print('Ответ сервера: ', result.decode('utf8'))
    if buf == "exit":
        break
s.close()

time.sleep(10)