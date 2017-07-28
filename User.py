class User:
	def __init__(self, name, balance, cart):
		self.name = name
		self.balance = balance
		self.cart = cart

	def add_to_cart(self, product, quantity):
		# TODO
		# 1. Can't add more than available stock
		# 2. Can't add if it doesn't have enough money to purchase
		current_stock = product.quantity

		if current_stock == 0:
			print("Sorry, item {} is out of stock. Please select a different item".format(product.id))
			return
		elif current_stock - quantity < 0:
			print('Cannot add more than what is available in stock')
			return

		# update quantities and balance
		self.cart[product] = self.cart.get(product, 0) + quantity
		product.quantity -= quantity

		# print added item
		print("{} {} is added to the shopping cart".format(quantity, product.name))

	def remove_from_cart(self, product, quantity):
		# TODO
		# 1. Cannot remove more than what's currently in cart
		# 2. Cannot remove if it's not in cart
		if product in self.cart:

			current_quantity = self.cart.get(product)

			if current_quantity < quantity:
				print('Cannot remove more than what is in the cart')
				return

			new_quantity = current_quantity - quantity

			if new_quantity == 0:
				self.cart.pop(product, None)
			else:
				self.cart[product] = new_quantity

			product.quantity += quantity
			print("{} {} is removed from the shopping cart".format(quantity, product.name))
		else:
			print('This item is not in the shopping cart')

	def clear(self):
		# TODO
		# update quantities
		for product, quantity in self.cart.items():
			product.quantity += quantity
		# remove everything from cart
		self.cart = {}
		print("All items are cleared from the shopping cart")

	def checkout(self):
		# TODO
		total_amount_due = 0
		bill_output = ["Checking out items ..."]

		if len(self.cart.items()) == 0:
			print("Cannot checkout empty cart")
			return False

		for product, quantity in sorted(self.cart.items(), key=lambda x: x[0].id):
			amount_due = product.price * quantity
			bill_output.append("{}/{}/${}".format(product.name, quantity, round(amount_due, 2)))
			total_amount_due += amount_due

		if total_amount_due > self.balance:
			print('Insufficient funds to purchase item(s)')
			print("${} required to purchase but current balance is ${}".format(round(total_amount_due, 2), round(self.balance, 2)))
			return False
		else:
			bill_output.append("Total amount due: ${}".format(round(total_amount_due, 2)))
			print("\n".join(bill_output))
			self.balance -= total_amount_due
			self.cart = {}
			return True