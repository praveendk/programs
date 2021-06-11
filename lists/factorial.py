#factorial program
#augumentative *=
print("Welcome to my program!")
number = int(input("Please enter the number: \n"))
if number < 0:
	print("No factorial for Negative numbers.")
elif number == 0:
	print("The factorial of 0 is 1")
else:
	i = 1
	x = 1
	for i in range(number):
		x = (i+1)*x
	i += 1
	print(x)


n2 = int(input("Please enter another number: \n"))
factorial = 1
for i in range(1, n2+1):
	factorial = factorial*i
print(factorial)
