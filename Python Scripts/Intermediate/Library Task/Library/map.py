import item

class Map(item.Item):
	def __init__(self, isbn, title, num_of_pages, location):
		super().__init__(isbn, title, num_of_pages)
		self.location = location
		
	def printInfo(self):
		print("ISBN:", self.isbn, "Title:" + self.title, "Number of Pages:", self.num_of_pages, "Map of:" + self.location)
		
		
