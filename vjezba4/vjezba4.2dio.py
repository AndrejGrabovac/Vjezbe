#echo_client.py
import socket
import datetime
from local_machine_info import print_machine_info

print_machine_info()

host = socket.gethostname()
port = 12345
client_socket = socket.socket()

client_socket.connect((host,port))

msg = " Tekst koji se salje serveru ".encode()
client_socket.sendall(msg)

str = input("Unesi tekst: ".encode())
client_socket.sendall(str.encode())

if(str == "andrej_grabovac"):
    print("Taj unos nije podrzan!")

print (datetime.datetime.now())

data = client_socket.recv(1024)

print(data)
client_socket.close()
