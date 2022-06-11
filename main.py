import random

# Red, Blue, Green, Yellow, Magenta, Cyan
# R, B, G, Y, M, C

chars = ["r", "b", "g", "y", "m", "c"]

def getIfCorrectPlace(correct, guessList):
	correctCount = 0
	for c,g in zip(correct, guessList):
		if c == g:
			correctCount += 1
	return correctCount

def getIfCorrectColor(correct, guessList):
	correctCount = 0
	for guess in guessList:
		if guess in correct:
			correctCount += 1
	return correctCount

def takeInputList(guess):
	return [letter for letter in input(f"Your guess nro {guess + 1}: ").lower() if letter in chars]

def makeCorrect():
	return [chars[random.randint(0, 5)] for i in range(4)]


if __name__ == "__main__":
	print(f"Characters: {', '.join(chars).upper()}")
	correct = makeCorrect()
	# print(correct)

	for i in range(15):
		guess = takeInputList(i)

		correctColor = getIfCorrectColor(correct,guess)

		correctPlace = getIfCorrectPlace(correct,guess)

		if correctPlace == 4:
			print("\033[95m\033[1mYOU WON!!!\033[0m")
			exit()

		print(f"Correct Color: \033[1m\033[91m{correctColor}\033[0m\nCorrect Place: \033[1m\033[91m{correctPlace}\033[0m")
	print("LOSER")
	print("Correct:",correct)
