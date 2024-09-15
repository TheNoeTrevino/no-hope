# How to get started

Do not run this on your actual machine in a random directory!

You will also need to install python, which is very easy with linux, I think.

Clone the repository:
```
git clone https://github.com/TheNoeTrevino/no-hope.git
```
I would prefer if we made branches and pull requests so things are easier to manage in the long run

## Usage

Make a file called key.txt in the same directory the script is. It would look something like this:

no-hope (folder)
| decrypt.py
| encrypt.py
| key.txt
| text.txt
|_

Make a file as a test, in this case test.txt, and fill it with some text, here is an example command:
```
echo 'This is not encrypted!' > test.txt
```
Then run the encryption script. It will output this, in addition to opening the bitcoin website in your browser:
```
$ python3 encrypt.py 
['test.txt']
b'0sU1m42-VAsvatbk3I1-77LQZQT_CFzIT2qK5U2irms='
give me 1mil bitcoin OR ELSE!
```
Lets check if this worked
```
$ cat test.txt 
gAAAAABm5nmEzE9aOMrfwaKCP9iENTdyHdVYW4d0NRyO9TyuXoV8QSAzJ-xJvp6CCecLDMd0kpv64O8ySAAKO4Hcbc8XitN4YvLIFFDlGLB3_dh38rP3cw8=%   
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
