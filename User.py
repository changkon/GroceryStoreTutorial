class User:
	def __init__(self, name, balance, cart={}):
		self.name = name
		self.balance = balance
		self.cart = cart