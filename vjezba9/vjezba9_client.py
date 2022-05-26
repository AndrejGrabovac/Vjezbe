import socket
import ssl
import pprint
from datetime import datetime
t1 = datetime.now()


def print_machine_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print("Host name: %s" % host_name)
    print("IP adress: %s" % ip_address)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ssl_sock = SSLContext.wrap_socket(
    s, ca_certs="certifikat.cert", cert_reqs=ssl.CERT_REQUIRED)

ssl_sock.connect(('localhost', 10023))
t2 = datetime.now()
print(ssl_sock.getpeername())
print(ssl_sock.cipher())
print(pprint.pformat(ssl_sock.getpeercert()))
total = t2 - t1
if __name__ == '__main__':
    print_machine_info()
    print("Vrijeme toliko: ", total)

ssl_sock.write("boo!")