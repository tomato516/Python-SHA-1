# Python-SHA-1 
Completed by: Jenny Choi  
This Python 2.7 program breaks SHA-1 hashes in a brute force manner.  
* User must input, as an argument, the hash value to the program 
* User must have the following password list(also provided in repository) in the **_same directory_** as the program: https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt

## How to run  
Run the program:  
```
$ python2 sha1BruteForce.py <INPUT HASH> 
```
Or: 
```
$ python2 sha1BruteForce.py <SALT TERM HASH> <PASSWORD HASH>
```
If match found, program shall output the password, number of guesses and duration to break the hash 

## Libraries used
```python
import hashlib
import time
import sys
```
1. hashlib: module containing an interface to the most popular hashing algorithms
2. time: module providing various time-related functions
3. sys: module providing access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter
## Solutions 
* Testing program hash: b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3:  
```
Password found: letmein
Number of guesses: 16
Duration to break hash: 0.14430809021 seconds
Goodbye!
```
* Medium hacker hash: 801cdea58224c921c21fd2b183ff28ffa910ce31:  
```
Password found: vjhtrhsvdctcegth
Number of guesses: 999968
Duration to break hash: 13.5483529568  seconds
Goodbye!
```

* Leet hacker salt term hash : f0744d60dd500c92c0d37c16174cc58d3c4bdd8e:
* Leet hacker password hash: ece4bb07f2580ed8b39aa52b7f7f918e43033ea1
```
Password found: harib
Number of guesses: 546372
Duration to break hash: 7.36961007118 seconds
Goodbye!
```

