import os
from utilities import decrypt

files = []

# make list of files
# TODO: if we decide to do recursion, we would have to do it here as well
for file in os.listdir():
    if (
        file == "decrypt.py"
        or file == "encrypt.py"
        or file == "utilities.py"
        or file == "key.txt"
        or file == "README.md"
        or file == ".gitignore"
    ):
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

# get info from keyfile
with open("key.txt", "rb") as key_file:
    key_data = key_file.read()
    salt = key_data[:16]
    secret_key = key_data[16:]

# decrypt
for file in files:
    with open(file, "rb") as _file:
        contents = _file.read()
        dec_content = decrypt(secret_key, contents)

        # write file with decrypted content
        with open(file, "wb") as _file:
            _file.write(dec_content)
