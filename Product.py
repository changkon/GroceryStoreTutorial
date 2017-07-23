class Product:
	def __init__(self, id, name, price, quantity):
		self.id = id
		self.name = name
		self.price = price
		self.quantity = quantity

	def print(self):
		# TODO
		print("{}, {}, ${}, {}".format(self.id, self.name, self.price, self.quantity))