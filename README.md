# How to get started

## Requirements
- Python 
- Git 

Clone the repository:

```
git clone https://github.com/TheNoeTrevino/no-hope.git
```

## Usage

Make a virtual environment:

```
python3 -m venv env
source env/bin/activate
pip3 install cryptogrgraphy pyinstaller
```

Compile the python code into binary via this command:

```
pyinstaller encrypt.py --onefile --hidden-import=cryptography --name <your-name-here>
pyinstaller decrypt.py --onefile --hidden-import=cryptography --name decryption
```

Then, run:

```
dist/encrypt
```

The files will be encrypted

To decrypt, run:

```
dist/decrypt
```

The encryptions and decryptions should work smoothly.

### NOTE:
This will only work if the encryption files are compiles on the same OS as the target, so if we want to lockdown a ubuntu 24.10, we need to compile on a 24.10

