#!/usr/bin/python3.6
import gnupg

class Decoder():
    def __init__(self):
        self.gpg = gnupg.GPG(gnupghome='/home/hackathon/.gnupg')

    def decode(self, message):
        message = b"-----BEGIN PGP MESSAGE-----\n" + message + b"\n-----END PGP MESSAGE-----\n"
        return str(self.gpg.decrypt(message, passphrase="noenter"))
