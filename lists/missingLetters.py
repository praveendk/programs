#program of missing letters
#for loop and list
print("Welcome to Missing letters program! \n")
userName = input("Please enter your name: \n")
print("hi " + userName + ", Welcome to the program!")
emailAddress = input("Please enter your email address: \n")
print("Thanks " + userName + " for providing your email address.")
missingLetters = ["di-b-t-s", "-n-ul-n", "g--c-s-", "nu--i-i-n"]
correctWords = ["diabetes", "insulin", "glucose", "nutrition"]
for i in range(len(missingLetters)):
	print("Fill the blanks with appropriate letters to make meaningful word \n" + missingLetters[i])
	userAnswer = input()
	if (userAnswer == correctWords[0]):
		print("You got it right! ")
	else:
		print("Oh, wrong answer!")