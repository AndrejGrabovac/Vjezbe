import socket

server_socket = socket.socket()
host = socket.gethostname()
port = 8080

server_socket.bind((host,port))

print ("waiting for connection...")
server_socket.listen(5)

while True:
    conn, addr = server_socket.accept()
    print ('got connection from '), addr
    str = 'Server saying Hi'.encode()
    conn.send(str)
    conn.close()