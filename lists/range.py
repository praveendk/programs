#Write a Python function to check whether a number is in a given range. 
try:
	number = int(input("Please enter the number between 1 to 100: \n"))
	def demo(number):
		if number in range(1, 101):
			print("Congradulations! The given number is in the range.")
		else:
			print("The given number is out of range")
	print(demo(number))
except:
	print("Only numbers between 1 to 100 are allowed")