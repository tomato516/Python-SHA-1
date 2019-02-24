# Python-SHA-1, By: Jenny Choi
This Python 2.7 program breaks SHA-1 hashes in a brute force manner.
* User must input, as an argument, the hash value to the program 
* User must have this password list in the _same directory_ as the program: https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt

## How to Use? 
Run the program: python2 <filename.py>  
User will be prompted to input hash value.  
If match found, program shall output the password, number of guesses and duration to break the hash 
* If the input hash value is a **_salted hash_**: 
* Input the **_salt term_** first 
* If a match is found, user will be asked if the hash is a salt term 
* User will be prompted to input **_password hash_** (this hash will be concatenated with salt term)  


## Solutions 
* Testing program hash: b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3 -> "letmein"
* Medium hacker hash: 801cdea58224c921c21fd2b183ff28ffa910ce31 -> "vjhtrhsvdctcegth"
* Leet hacker salt term hash : f0744d60dd500c92c0d37c16174cc58d3c4bdd8e -> "slayer"
* Leet hacker password hash(_must be concatenated with salt term hash_): ece4bb07f2580ed8b39aa52b7f7f918e43033ea1 -> "harib" 


