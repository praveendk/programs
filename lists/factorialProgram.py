#Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument. 
try:
	number = int(input("Please enter any non-negative integer to calculate its factorial: \n"))
	def demo(number):
		factorial = 1
		for i in range(1, number+1):
			factorial *= i
		return factorial
	print(demo(number))
except:
	print("invalid input: Only positive integers are allowed.")
