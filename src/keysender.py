#!/usr/bin/python3.6
from socketserver import TCPServer, StreamRequestHandler
import socket
import logging


class Handler(StreamRequestHandler):
    def handle(self):
        self.data = self.rfile.readline().strip()
        logging.info("From <%s>: %s" % (self.client_address, self.data))

        if self.data == b"Hackathon":
            self.wfile.write(self.data.upper() + "\r\n".encode("utf-8"))


class Server(TCPServer):
    SYSTEMD_FIRST_SOCKET_FD = 3

    def __init__(self, server_address, handler_cls):
        TCPServer.__init__(
            self, server_address, handler_cls, bind_and_activate=False)

        self.socket = socket.fromfd(
            self.SYSTEMD_FIRST_SOCKET_FD, self.address_family, self.socket_type)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    HOST, PORT = "localhost", 1338
    server = Server((HOST, PORT), Handler)
    server.serve_forever()
