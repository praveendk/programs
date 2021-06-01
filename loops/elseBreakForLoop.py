# else will not execute if the break used
for x in range(100):
  if x == 98:
    break
  print(x)
else:
  print("Happy Ending")