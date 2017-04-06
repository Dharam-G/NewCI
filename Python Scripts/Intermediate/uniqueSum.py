def sum(a, b, c):

	if (a == b == c):
		print("a + b + c = 0")
	
	elif (a == b):
		print("a + b + c =", c)
	
	elif (a == c):
		print("a + b + c =", b)
	
	elif (b == c):
		print("a + b + c =", a)
	
	elif (a != b != c):
		d = a + b + c
		print("a + b + c =", d)
		
sum(int(input("a = ")), int(input("b = ")), int(input("c = ")))