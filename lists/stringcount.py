#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. 
print("Welcome to the program!")
string = input("Please enter any word including both small and capital letters: \n")
stringLength = len(string)

def demo(string):
	capital = 0
	small = 0
	for i in string:
		y = ord(i)
		if y  in range(65, 97):
			capital += 1
		elif y in range(97, 123):
			small += 1
		else:
			print("nothing")
	print("The total number of letters in the given input are ", stringLength)
	print("The number of Capital letters in the given input is ", capital)
	print("The number of small letters used in the given input are ", small)
print(demo(string))
