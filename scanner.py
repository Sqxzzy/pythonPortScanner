# Sqxzzy

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input("Kérlek írd be az IP címet: ")
port = int(input("Kérlek add meg a kívánt portot: "))

def portScanner(port):
    if s.connect_ex((host, port)):
        print("Ez a port nem nyitott.")
    else:
        print("Ez a port nyitott.")
portScanner(port)
