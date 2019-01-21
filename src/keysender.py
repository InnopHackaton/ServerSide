#!/usr/bin/python3.6
import socket
import logging


with open("pubkey.asc", "rb") as keyfile:
        key = keyfile.read()

logging.basicConfig(level=logging.INFO)
sock = socket.socket()
sock.bind(('', 1338))

while True:
    sock.listen(1)
    conn, addr = sock.accept()
    logging.info("<%s> connected" % (addr[0]))

    conn.send(key)

    conn.close()

