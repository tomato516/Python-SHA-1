import hashlib 
import time 
import sys 

#Jenny Choi: Blockchain & Applications Assignment #2
#get user input as an argument  
sha1hash = sys.argv[1]
start = time.time()

#open password file 
filename = "10-million-password-list-top-1000000.txt"
listOfPasswords = str(open(filename).read())
counter = 0

#loop & check for a match  
for guess in listOfPasswords.split('\n'): 
	#hash each guess to compare to user's hash 
	firstGuess = hashlib.sha1(bytes(guess)).hexdigest()
	if firstGuess == sha1hash:
		counter += 1 
		end = time.time()
		#time of search
		noSaltTime = end - start

		print "==========================================================="
		print "Password found: ", guess
		print "Number of guesses: ", counter 
		print "Duration to break hash: ", noSaltTime, " seconds"

		#check if user input more than one argument(salted hash)
		while len(sys.argv) == 3:

			#previous password becomes the salt term 
			saltTerm = guess 

			#get user input for second hash 
			sha1hash1 = sys.argv[2]
			saltStart = time.time()

			#loop & check for whole hash 
			for guess1 in listOfPasswords.split('\n'):
				secondGuess = hashlib.sha1(bytes(saltTerm + guess1)).hexdigest()
				if secondGuess == sha1hash1:
					counter += 1
					saltEnd = time.time()
					#combined time of search 
					saltTime = (saltEnd - saltStart) + noSaltTime

					print "==========================================================="
					print "Password found: ", guess1
					print "Number of guesses: ", counter
					print "Duration to break hash: ", saltTime, " seconds"
					print "Goodbye!"
					quit()

				elif secondGuess != sha1hash1:
					counter += 1
					print "Trying password ", str(saltTerm + guess1),"does not match, trying next..."

			#no match in file 
			print "==========================================================="
			print "Sorry, password not in database"


		#if user input one argument, exit program
		print "Goodbye!"
		quit()

	elif firstGuess != sha1hash:
		counter += 1 
		print "Trying password ", str(guess),"does not match, trying next..."

#no match in file 
print "==========================================================="
print "Sorry, password not in database"
quit()









