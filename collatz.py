print("Welcome to Collatz! \n")
number = int(input("Please enter the number \n"))
i = number
def collatz(number):
	even = (number%2 == 0)
	if (even == True):
	    return number//2
	else:
	    return 3*number+1

while i != 1:
    print ("number is ",i)
    i = collatz(i)