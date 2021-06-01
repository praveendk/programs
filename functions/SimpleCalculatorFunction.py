#building functions in calculator and calling them
#using global and local variables

print("Hello user, Welcome to Simple Calculator!")
x = "Please type the username registered with us"
for userName in range(1, 6):
  print(x)
  userName = input()

  if userName == "lakshmi":
    break
print("Welcome Lakshmi")


firstNumber = int(input("Please type the first number: \n"))
secondNumber = int(input("Please type the second number: \n"))
def sum():
  return firstNumber + secondNumber

def sub():
  return firstNumber - secondNumber

def product():
  return firstNumber * secondNumber

def division():
  return firstNumber // secondNumber

print("Calculator results are as follows \n")
print("The addition, difference, product and division of " + str(firstNumber) + " and " + str(secondNumber) +  "are " + str(sum()) + ", " + str(sub()) + ", " + str(product()) + ", " + str(division()) + " respectively.")