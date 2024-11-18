import os
from utilities import decrypt, generate_key

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

# TODO: change this dir to the home for the current user
for root, dirs, filenames in os.walk("/Users/noetrevino/Desktop/"):
    dirs[:] = [d for d in dirs if d not in excluded_dirs]

    for file in filenames:
        if file in excluded_files:
            continue
        files.append(os.path.join(root, file))

print("Files to decrypt:", files)

# enter the pass in the decryption file
password: bytes = input("enter password: ").encode()  # str -> binary

# enter the salt in the decryption file
salt: bytes = input("enter salt: ").encode()

secret_key = generate_key(password, salt)
# print("\n", "secret key: ",secret_key)

# TODO: remove this
print("\n", "generated Secret Key:", secret_key)

for file in files:
    with open(file, "rb") as _file:
        contents = _file.read()
        dec_content = decrypt(secret_key, contents)

    with open(file, "wb") as _file:
        _file.write(dec_content)

print("decryption successful")
