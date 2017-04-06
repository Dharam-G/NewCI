from abc import ABC, abstractmethod

class Item(ABC):
	def __init__(self, isbn, title, num_of_pages):
		self.isbn = isbn
		self.title = title
		self.num_of_pages = num_of_pages