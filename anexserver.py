import socket
import sys

s = socket.socket()
host = socket.gethostname()
print(" Serverin quruldugu host : ", host)
port = 8080
s.bind((host,port))
name = input(str("Nickini yaz: "))
print("")
print("Server is waiting for incoming connections")
print("")
s.listen(1)
conn, addr = s.accept()
print("Baglanti qebul edildi")
print("")
s_name = conn.recv(1024)
s_name = s_name.decode()
print(s_name, "chata qosuldu")
conn.send(name.encode())

while 1:
    message = input(str("Mesajini daxil et: "))
    conn.send(message.encode())
    print("Gonderildi")
    print("")
    message = conn.recv(1024)
    message = message.decode()
    print(s_name, ":" ,message)
    print("")