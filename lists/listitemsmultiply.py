#Write a Python function to multiply all the numbers in a list. 
def multiply(numbers):
	product = 1
	for i in numbers:
		product *= i
	return product
print(multiply((3, 4, 5)))
y = []
n1 = int(input("Please enter the first number: \n"))
n2 = int(input("Please enter the second number: \n"))
n3 = int(input("Please enter the third number: \n"))

y.insert(0, n1)(1, n2)(2, n3)
print(sum(y))