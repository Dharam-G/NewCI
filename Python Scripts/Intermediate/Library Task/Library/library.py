from item import Item
from person import Person
from book import Book
from magazine import Magazine
from map import Map

class Library():
	
	def __init__(self):
		self.itemList = []
		self.peopleList = []
		
	def addItem(self):
		#Add information for new item
		addItem = str(input("Would you like to add an item? "))
		#loop to ask whether item is to be added or not
		while(addItem.lower() == "yes"):
			itemType = str(input("What type of item would you like to add? Book, Map, or Magazine? "))
			
			if(itemType.lower() == "book"):
				new_item = Book(int(input("ISBN: ")),str(input("Title: ")),int(input("Number of Pages: ")),bool(input("Hardback? True or False: ")))
				self.itemList.append(new_item)
				
			elif(itemType.lower() == "map"):
				new_item = Map(int(input("ISBN: ")), str(input("Title: ")), int(input("Number of Pages: ")), str(input("Location of Map: ")))
				self.itemList.append(new_item)
				
			elif(itemType.lower() == "magazine"):
				new_item = Magazine(int(input("ISBN: ")), str(input("Title: ")), int(input("Number of Pages: ")), int(input("Issue Number: ")))
				self.itemList.append(new_item)
			
			else:
				print("Invalid")
				continue
			
			for i in range(len(self.itemList)):
				print(self.itemList[i].title)
					
			addItem = str(input("Would you like to add an item? "))
			
		print("Number of items added:", len(self.itemList))
		
	def viewItems(self):
		for i in self.itemList:
			print("ISBN:", i.isbn, "Title:", i.title)
	'''
	def removeItem(self):
		for i in self.itemList:
			if i.id == ID:
				self.itemList.remove(i)'''
				
	def addPerson(self):
		#Add information for new item
		addPerson = str(input("Would you like to register a new person? "))
		#loop to ask whether item is to be added or not
		if(addPerson.lower() == "yes"):
			
			new_person = Person(int(input("ID: ")),str(input("Name: ")),int(input("Age: ")))
			self.peopleList.append(new_person)
				
		else:
			print("Invalid")
			
		for i in range(len(self.personList)):
			print(self.personList[i].name)
					
		addPerson = str(input("Would you like to register another user? "))
			
		print("Number of items added:", len(self.personList))
		'''
	def viewPerson(self):
		
		
	def removePerson(self, ID):
		for i in self.people:
			if i.id == ID:
				self.peopleList.remove(i)
		'''

		
mylib = Library()
mylib.addItem()
mylib.viewItems()
mylib.addPerson()