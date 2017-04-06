def operators(x, y, switch):
	
	print("x =", x)
	print("y =", y)
	
	if (x == 0 or y == 0):
		
		if (x == 0 and y == 0):
			print("x + y =", x)
		
		elif (x == 0):
			print("x + y =", y)
		
		elif (y == 0):
			print("x + y =", z)
			
	else:
	
		if switch == True:
			z = x + y
			print("x + y =", z)
	
		else:
			z = x * y
			print("x * y =", z)
	
operators(5, 6, True)