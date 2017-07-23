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
		# TODO
		available_stock = filter(lambda x: x.quantity > 0, self.stock)
		available_stock_sorted = sorted(available_stock, key=lambda x: x.id)
		for stock in available_stock_sorted:
			stock.print()