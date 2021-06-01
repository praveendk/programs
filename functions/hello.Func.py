#building functions and calling them
def hello():
  print("Hello Lakshmi")
  firstNumber = int(input("Please enter the first number \n"))
  secondNumber = int(input("Please enter the second number \n"))
  sum = firstNumber + secondNumber
  print("The sum of " + str(firstNumber) + " and " + str(secondNumber) + " is " + str(sum) + ".")

hello()
hello()