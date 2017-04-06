from functools import partial

def multiply(x,y):
	return x*y
	
double = partial(multiply,2)
triple = partial(multiply,3)

a = int(input("Enter a number to double: "))
print(double(a))

b = int(input("Enter a number to triple: "))
print(triple(b))