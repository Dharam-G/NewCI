list_length = 10

list = [0] * list_length

print(list)

for i in range(list_length):
	list[i] = i+1
	
print(list)

for i in range(list_length):
	list[i] = ((i+1)*10)
	
print(list)

