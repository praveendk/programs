#quiz program
#lists and for loop
print("Welcome to the numbers quiz!")
try:
	userName = input("Please enter your name: \n")
	city = input("Please enter your name of the city: \n")
	print("Hi " + userName + ", Thanks for providing your name of the city " + city)
	if not type(userName) or type(city) is int:
		raise typeError("Numbers are not allowed.")
