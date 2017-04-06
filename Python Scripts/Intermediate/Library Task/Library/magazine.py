import item

class Magazine(item.Item):
	def __init__(self, isbn, title, num_of_pages, issue_number):
		super().__init__(isbn, title, num_of_pages)
		self.issue_number = issue_number
	
	def printInfo(self):
		print("ISBN:", self.isbn, "Title: " + self.title, "Number of Pages:", self.num_of_pages, "Issue number:", self.issue_number)
		
