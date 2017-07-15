class GroceryStore:
	def __init__(self, name, stock):
		self.name = name
		self.stock = stock

	def print_available_products(self):
		# TODO
		print(len(self.stock))
		pass