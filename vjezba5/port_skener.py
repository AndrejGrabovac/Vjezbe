import socket
import subprocess
import sys
from datetime import datetime

subprocess.call('clear', shell=True)

remoteServer = input("Molim vas unesite adresu hosta koju zelite testirati: ")
remoteServerIP = socket.gethostbyname(remoteServer)

print("-" * 60)
print("Skeniram host: ", remoteServerIP)
print("-" * 60)

port1 = int(input("Unesite prvi port: "))
port2 = int(input("Unesite drugi port: "))

t1 = datetime.now()

try:
    for port in range(port1, port2):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}:           Otvoren".format(port))
            sock.close()

except KeyboardInterrupt:
    print("Pritisnio si CTRL+C")
    sys.exit()

except socket.gaierror:
    print("Nemoguće dohvatiti hosta. IZLAZIM!")
    sys.exit()

except socket.error:
    print("Nemoguće se spojiti na server")
    sys.exit()

t2 = datetime.now()

total = t2 - t1

print("Skeniranje zavrseno za: ", total)
