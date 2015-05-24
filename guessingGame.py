import random

def getRandomInt():
	return random.randint(1,10)

def hello():
	print("Try and guess the number the computer comes up with. The number is between 1 and 10. \nYou have 3 guesses. If you need help, type 'HELP' \n\nGood luck!")
	pass

def help(guessesTaken):
	print("Guess you have already tried: {} \nNumber of guesses remaining: {} ".format(", ".join(str(guess) for guess in guessesTaken), 3-len(guessesTaken)))
	pass

def endGame(thePlayerWon, numberToGuess, numOfGuesses=3):
	if thePlayerWon and numOfGuesses == 1:
		print("Congratulations! You won in 1 guess")
	if thePlayerWon:
		print("Congratulations! You won in {} guesses".format(str(numOfGuesses)))
	else:
		print("Sorry! The number you needed to guess was {}".format(str(numberToGuess)))

def start():
	hello()
	game()

def game(): 
	numToGuess = str(getRandomInt())
	print(numToGuess)
	guessesTaken = []
	while len(guessesTaken) < 3:
		guess = input("Make a guess between 1 and 10: ")
		if str(guess)=="HELP":
			help(guessesTaken)
			continue
		try:
			if int(guess)<1 or int(guess)>10:
				print("Please enter a guess between 1 and 10")
				continue
			elif int(guess) < int(numToGuess):
				print("Your guess is too low.")
				guessesTaken.append(guess)
				continue
			elif int(guess) > int(numToGuess):
				print("Your guess is too high.")
				guessesTaken.append(guess)
				continue
			elif str(guess) == str(numToGuess):
				print("You guessed correctly!")
				endGame(True, numToGuess, len(guessesTaken)+1)
		except: 
			print("Please only enter numbers between 1 and 10 or 'HELP' if you need help")
	endGame(False, numToGuess)

start()

