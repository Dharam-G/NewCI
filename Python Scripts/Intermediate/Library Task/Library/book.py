import item

class Book(item.Item):
	def __init__(self, isbn, title, num_of_pages, hardback):
		super().__init__(isbn, title, num_of_pages)
		self.hardback = hardback
		
	def hardBack(self):
		if (self.hardback.lower() == "yes"):
			print("This book has a hardback cover")
		else:
			print("This book does NOT have a hardback cover")
			
	def printInfo(self):
		print("ISBN:", self.isbn, "Title: " + self.title, "Number of pages:", self.num_of_pages, "Hardback cover? " + self.hardback)
			
	def newBook(self):
		newBook = (str(input(self.isbn)))