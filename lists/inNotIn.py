#in and not in 
i = ["cat", "bat", "rat", "elephant"]
for j  in range(len(i)):
	print("Please type the word you see below: \n ",  i[j])
	word = input()
	if word not in i:
			print("wrong input")
	else:
		print("Good")