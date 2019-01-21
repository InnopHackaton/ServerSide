#!/usr/bin/python3
"""Server for multithreaded (asynchronous) chat application."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from coder import Encoder, Decoder
import logging
import configparser

def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        logging.info("%s:%s has connected." % client_address)
        private("Type your login: ", client)
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""

    name = recv(client).strip()
    welcome = 'Welcome %s!\n' % name
    private(welcome, client)
    clients[client] = name
    send("I AM IN!\n", client)

    while True:
        msg = recv(client)
        if msg is "":
            send("BYE", client)
            client.close()
            del clients[client]
            break
        send(msg, client)


def private(msg, rspt):
    """To one client"""
    rspt.send(encoder.encode("%s" % msg))


def send(msg, client):
    for sock in clients:
        if sock is not client:
            sock.send(encoder.encode("%s: %s" % (clients[client], msg)))


def recv(client):
    return decoder.decode(client.recv(BUFSIZ))


config = configparser.ConfigParser()
config.read('configs/config.ini')

clients = {}
addresses = {}

HOST = ''
PORT = int(config['DEFAULT']['MES_PORT'])
BUFSIZ = 6144
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    encoder, decoder = Encoder(), Decoder()
    SERVER.listen(5)
    logging.info("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
