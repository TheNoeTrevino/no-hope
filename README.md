# How to get started

First off you will not want to run this on your actual machine, so please be careful with this. 

You will also need to install python, which is very easy with linux, I think.

Make a file called key.txt in the same directory the script is. It would look something like this:

no-hope (folder)
| decrypt.py
| encrypt.py
| key.txt
| text.txt
|_

Make a file as a test, in this case test.txt, and fill it with some text, here is an example command:
```
echo 'This is working just fine!' > test.txt
```
Then run the decrypt script:
```
python3 decrypt.py 
```
the output should show this:
