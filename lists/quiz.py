#quiz program
#lists and for loop
print("Welcome to the numbers quiz!")
userName = input("Please enter your name: \n")
emailAddress = input("Please enter your email address: \n")
print("Hi " + userName + ", Thanks for providing your email address " + emailAddress)
i = 0
while i != 1:
	print("Please press 1 to continue.")
	number = int(input())
	if number == 1:
		break
print("Important note: This quiz has negative marking: For every wrong answer, you will loose the marks. Therefore,  please verify your answer before submitting")
questions = [1, 2, 3, 4, 5]
answers = ["one", "two", "three", "four", "five"]
k = 0
for j in range(len(questions)):
	print("Please type the numbers in English words: " + questions[j])
	userAnswer = input()
	if userAnswer == answers[j]:
		print("Congratulations! you got it right!")
		k += 1
	else:
		print("wrong answer!")
		k -= 1