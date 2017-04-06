list_length = 10

#Create empty list and print
list = [0] * list_length

print(list)

#Give values to list and print
for i in range(list_length):
	list[i] = i+1
	
print(list)

#Nultiply list by user given integer and print
j = int(input())
for i in range(list_length):
	list[i] = ((i+1)*j)
	
print(list)
