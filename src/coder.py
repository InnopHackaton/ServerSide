#!/usr/bin/python3.6
import gnupg
from Crypto.Cipher import AES
import base64

class Decoder():
    def __init__(self):
        self.gpg = gnupg.GPG(gnupghome='/home/hackathon/.gnupg')

    def decode(self, message):
        message = b"-----BEGIN PGP MESSAGE-----\n" + message + b"\n-----END PGP MESSAGE-----\n"
        return str(self.gpg.decrypt(message, passphrase="noenter"))

class Encoder():
    def __init__(self):
        self.secret_key = '1234567890123456'
        self.cipher = AES.new(self.secret_key,AES.MODE_ECB) 

    def encode(self, message):
        return base64.b64encode(self.cipher.encrypt(message.rjust(32)))
