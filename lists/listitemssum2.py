#Write a Python function to sum all the numbers in a list.
#function and loops
def sum(numbers):
	total = 0
	for x in numbers:
		total += x
		return total
y = [0, 1, 2]
y[0] = int(input("Please enter the first number: \n"))
y[1] = int(input("Please enter the second number: \n"))
y[2] = int(input("Please enter the third number: \n"))
print(sum((y)))