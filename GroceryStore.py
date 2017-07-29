class GroceryStore:
	def __init__(self, id, name, stock):
		self.id = id
		self.name = name
		self.stock = stock

	def get_product(self, product_id):
		# check if enough quantity
		product = next(p for p in self.stock if p.id == product_id)
		return product

	def print_available_products(self):
		"""
		TODO
		Prints product information for available stock. Printing is sorted by its id value descending.
		:return: prints formatted product information sorted by id descending
		"""
		pass