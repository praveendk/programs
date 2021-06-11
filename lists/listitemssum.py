# Write a Python function to sum all the numbers in a list. 
x = [0, 1, 2]
x[0] = int(input("Please enter the first number \n"))
x[1] = int(input("Please enter the second number \n"))
x[2] = int(input("Please enter the third number \n"))

print(x)
a = 0
i = 0
for i in x:
	a = i+a
	i += 1
print(a)