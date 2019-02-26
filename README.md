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


## Solutions 
* Testing program hash: b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3 
![First Solution]
(https://github.com/tomato516/images/blob/master/sha1FirstHashSolution.png)

* Medium hacker hash: 801cdea58224c921c21fd2b183ff28ffa910ce31 
![Second Solution]
(https://github.com/tomato516/images/blob/master/sha1MediumHashSolution.png)

* Leet hacker salt term hash : f0744d60dd500c92c0d37c16174cc58d3c4bdd8e -> "slayer"
![Third Solution]
(https://github.com/tomato516/images/blob/master/sha1LeetHackerSolution.png)
