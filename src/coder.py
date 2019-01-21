#!/usr/bin/python3.6
import gnupg
from Crypto.Cipher import AES
import base64
import configparser

class Decoder():
    def __init__(self):
        self.gpg = gnupg.GPG(gnupghome='/root/.gnupg')

        config = configparser.ConfigParser()
        config.read('configs/config.ini')
        self.passphrase = config["DEFAULT"]["PASSPHRASE"]
 
    def decode(self, message):
        message = b"-----BEGIN PGP MESSAGE-----\n" + message + b"\n-----END PGP MESSAGE-----\n"
        return str(self.gpg.decrypt(message, passphrase=self.passphrase))

class Encoder():
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('configs/config.ini')

        self.secret_key = config["DEFAULT"]["SECRET_KEY"]
        self.cipher = AES.new(self.secret_key,AES.MODE_ECB) 

    def encode(self, message):
        return base64.b64encode(self.cipher.encrypt(message.rjust(32)))
