# How to get started

Do not run this on your actual machine in a random directory! It will encrypt anything that is not a directory and its kind of annoying to fix sometimes. (speaking from the experience of messing it up like 10 times in a row)

You will also need to install python, which is very easy with linux, I think.

### Clone the repository:
```
git clone https://github.com/TheNoeTrevino/no-hope.git
```
I would personally prefer if we made branches and pull requests so things are easier to manage in the long run, but we can talk about this.

## Usage

Make a file called key.txt in the same directory the script is. It would look something like this:

no-hope (folder)
| decrypt.py<br>
| encrypt.py<br>
| key.txt<br>
| text.txt<br>
|_

Make a virtual environment:

```
python3 -m venv env
pip3 install cryptogrgraphy
```

Make a file as a test, in this case test.txt, and fill it with some text, here is an example command:
```
echo 'This is not encrypted!' > test.txt
```
Then run the encryption script. It will output this, in addition to opening the bitcoin website in your browser:
```
$ python3 encrypt.py
Files to encrypt: ['test.txt']
Give me one million bitcoin OR ELSE I WILL DELETE THE KEY FOREVER
b'ET\xa3$\xdd\xbb\x90\xb8\x10\xed\xfa\x00\xa2\xbe\xbb\xa9\xc3Mr\x0c\xa8\xe7p>z\xd3\x01\xc8\x82\xfa\x05\xb4'
```
Lets check if this worked
```
$ cat test.txt 
q��d���3�W	���fp�u��S�7�Wu����Sv�s�$��>dވ[����h�<A6Wl~k?}N�Ex"�S�5w�`���9%    
```
These are the encrypted contents of the file!
Now let us decrypt them by running the decryption script, which is also going to show us an array on files that have gotten decrypted
```
$ python3 decrypt.py 
['test.txt']
```
Lets check if it worked
```
$ cat test.txt 
This is not encrypted!
```
Woohoo! We are back to normal!
