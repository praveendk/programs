#exceptional handling 
#zeroDivideBy program
#exceptions and try
def vln(divideBy):
  try:
    return 42/divideBy


  except zeroDivisionError: 

    print("Zero division: Invalid argument")


print(vln(2))
print(vln(1))
print(vln(0))
print(vln(30))