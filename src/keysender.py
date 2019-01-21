#!/usr/bin/python3
import socket
import logging
import configparser

config = configparser.ConfigParser()
config.read('configs/config.ini')
PORT = int(config['DEFAULT']['KEY_PORT'])
with open("pubkey.asc", "rb") as keyfile:
        key = keyfile.read()

logging.basicConfig(level=logging.INFO)
sock = socket.socket()
sock.bind(('', PORT))

while True:
    sock.listen(1)
    conn, addr = sock.accept()
    logging.info("<%s> connected" % (addr[0]))

    conn.send(key)

    conn.close()

