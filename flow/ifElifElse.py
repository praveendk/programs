# finding the given number is even or odd
number = int(input("Please enter the number \n"))
result = number % 2
if result == 0:
  print("The given number is Even number")
elif result == 1:
  print("The given number is Odd number")
else:
  print("You have not provided integer")