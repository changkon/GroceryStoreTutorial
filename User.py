class User:
	def __init__(self, name, balance, cart):
		self.name = name
		self.balance = balance
		self.cart = cart

	def add_to_cart(self, product, quantity):
		"""
		TODO
		Should add to user cart if successful addition. Adding to cart should create a key in the cart dictionary variable and update the quantity value.
		Product quantity should also decrease.
		Should handle the scenarios:
		1. Can't add more than available stock
		2. Can't add out of stock items
		:param product:
		:param quantity:
		:return:
		"""
		pass

	def remove_from_cart(self, product, quantity):
		"""
		TODO
		Should remove desired quantity from user cart. If the quantity in the cart is zero, its key should be removed from the cart dictionary variable.
		Successful removal from cart should restore the product quantity.
		Should handle:
		1. Cannot remove more than what's currently in cart
		2. Cannot remove product if it's not in the cart
		:param product:
		:param quantity:
		:return:
		"""
		pass

	def clear(self):
		"""
		TODO
		Clears user cart and displays message.
		Should empty cart and restore product quantity.
		Message is displayed even if cart is empty
		:return:
		"""
		pass

	def checkout(self):
		"""
		TODO
		Prints bill if there is successful checkout. Checkout checks if the user has sufficient funds to checkout cart. If sufficient, it empties cart and updates user balance.
		Otherwise, message is displayed. Unsuccessful checkout should not affect product quantity or user cart. Cannot checkout empty cart
		Should handle
		1. Checking out empty cart display message
		2. Insufficient funds to checkout cart
		3. Sufficient funds to checkout cart
		:return:
		"""
		pass