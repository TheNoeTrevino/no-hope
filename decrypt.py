import os
from cryptography.fernet import Fernet

files = []

# TODO: make this also recursively decrypt like the encrypt file
for file in os.listdir():
    # avoid acciently locking out current progress
    if file == "decrypt.py" or file == "encrypt.py" or file == "key.txt":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

with open("key.txt", "rb") as key:
    secretkey = key.read()

for file in files:
    with open(file, "rb") as _file:
        contents = _file.read()
    dec_content = Fernet(secretkey).decrypt(contents)
    with open(file, "wb") as _file:
        _file.write(dec_content)

#     enc_content = Fernet(key).encrypt(contents)
#     with open(file, "wb") as _file:
#         _file.write(enc_content)
