import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


# NOTE: I included links to the documentation for some
# https://cryptography.io/en/latest/hazmat/primitives/key-derivation-functions/
def generate_key(password, salt):

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    return kdf.derive(password)


# AES-GCM encryption and decryption, from hollies canvas comment
# NOTE: https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/
def encrypt(key, data):
    nonce = os.urandom(12)
    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(data) + encryptor.finalize()
    return nonce + ciphertext + encryptor.tag


def decrypt(key, data):
    nonce = data[:12]
    tag = data[-16:]
    ciphertext = data[12:-16]
    cipher = Cipher(
        algorithms.AES(key), modes.GCM(nonce, tag), backend=default_backend()
    )
    decryptor = cipher.decryptor()
    return decryptor.update(ciphertext) + decryptor.finalize()
