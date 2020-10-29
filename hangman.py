import collections

wordToGuess = "hangman"
indexesCorrect = []
guessedLetter = []
guesses = 0

if __name__ == '__main__':

	correctWord = {}
	for i , letter in enumerate(wordToGuess):
		correctWord[i] = letter

	notGuessed = True
	while notGuessed:
		l = input("Enter a letter : ")
		guesses += 1
		if len(l) != 1:
			print("Enter a single character.")
			continue
		if l not in guessedLetter:
			if l in wordToGuess:
				for letter in correctWord:
					if l == correctWord[letter]:
						indexesCorrect.append(letter)
			else:
				print("The letter " + l + " is not in the word")
			guessedLetter.append(l)
		else:
			print("You already guessed " + l)

		wordGuessedSoFar = ''
		indexesCorrect.sort()
		for i in range(len(wordToGuess)):
			if i in indexesCorrect:
				wordGuessedSoFar += wordToGuess[i]
			else:
				wordGuessedSoFar += "_"
		print("Progress : " + wordGuessedSoFar)

		if wordGuessedSoFar == wordToGuess:
			print("WINNER! \nGuessed in " + str(guesses) + " turns")
			notGuessed = False