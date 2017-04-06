def winner(a, b):

	if (a > 21 or b > 21):
	
		if (a > 21 and b > 21):
			print(0)
		
		elif (a > 21):
			print("b wins with", b)
		
		elif (b > 21):
			print("a wins with", a)
		
	elif (a > b):
		print("a wins with", a)
	
	elif (b > a):
		print("b wins with", b)
	
	elif (a == b):
		print("No winner. a and b both had the same hand of", a)
		
winner(int(input("Player a hand value: ")), int(input("Playerb hand value: ")))
