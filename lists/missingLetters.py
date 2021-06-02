#program of missing letters
#for loop and list
print("Welcome to Missing letters program! \n")
userName = input("Please enter your name: \n")
print("hi " + userName + ", Welcome to the program!")
emailAddress = input("Please enter your email address: \n")
print("Thanks " + userName + " for providing your email address.")
missingLetters = ["di-b-t-s", "-n-ul-n", "g--c-s-", "nu--i-i-n", "s-n-o-", "-e-on-s", "p-ot--n", "-e-l-h", "-lu--m-t-r", "d-c-o-"]
correctWords = ["diabetes", "insulin", "glucose", "nutrition", "sensor", "ketones", "protein", "health", "glucometer", "doctor"]
j = 0
for i in range(len(missingLetters)):
	print("Fill the blanks with appropriate letters to make meaningful word \n" + missingLetters[i])
	userAnswer = input()
	if (userAnswer == correctWords[i]):
		print("You got it right! ")
		j += 1
	else:
		print("Oh, wrong answer!")

print("Dear " + userName + ", Your score: ")
if j <= 0:
	print("You scored very low. Please improve")
else:
	print("Congratulations! you have scored " + str(j/len(missingLetters)*100) + "%")