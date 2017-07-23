import unittest
import GroceryStoreMain
from User import User
from contextlib import contextmanager
from io import StringIO
import sys

@contextmanager
def capture():
	new_out, new_err = StringIO(), StringIO()
	old_out, old_err = sys.stdout, sys.stderr
	try:
		sys.stdout, sys.stderr = new_out, new_err
		yield sys.stdout, sys.stderr
	finally:
		sys.stdout, sys.stderr = old_out, old_err

class TestGroceryStore(unittest.TestCase):

	def setUp(self):
		self.grocery_store = GroceryStoreMain.initialise()
		starting_balance = 50
		user_name = "Chang Kon"
		self.user = User(user_name, starting_balance)

	def test_product_print(self):
		bread = self.grocery_store.get_product(1)

		with capture() as (out, err):
			bread.print()

		output = out.getvalue().strip()
		expected_output = "1, Fresh toast bread white, $3.99, 20"
		self.assertEquals(expected_output, output)

	def test_grocery_store_print_initial_products(self):
		with capture() as (out, err):
			self.grocery_store.print_available_products()

		output = out.getvalue().strip()
		expected_output = [
			"1, Fresh toast bread white, $3.99, 20",
			"2, Low-fat milk, $4.8, 10",
			"3, V-energy drink, $2.75, 10",
			"4, Fresh garlic, $1.98, 5",
			"5, Pineapple, $3.6, 6",
			"6, Mango, $1.89, 4",
			"7, Snickers chocolate bar, $1.8, 20",
			"8, Broccoli, $1.47, 11",
			"9, Washed Potato, $2.98, 7",
			"10, Good-morning cereal, $5.6, 10",
			"11, Rose apple, $4.98, 5",
			"12, Avocado, $4.99, 5",
			"13, Bananas, $2.96, 4",
			"14, Kiwi fruit green, $2.45, 10",
			"15, Rock melon, $7.98, 2",
			"16, Lettuce, $2.99, 12",
			"17, Chocolate block, $3.59, 10"
			]
		self.assertEquals("\n".join(expected_output), output)

	def test_grocery_store_print_products_does_not_print_out_of_stock_products(self):
		# update products
		garlic = self.grocery_store.get_product(4)
		garlic.quantity = 0
		chocolate = self.grocery_store.get_product(17)
		chocolate.quantity = 7
		banana = self.grocery_store.get_product(13)
		banana.quantity = 0

		with capture() as (out, err):
			self.grocery_store.print_available_products()

		output = out.getvalue().strip()
		expected_output = [
			"1, Fresh toast bread white, $3.99, 20",
			"2, Low-fat milk, $4.8, 10",
			"3, V-energy drink, $2.75, 10",
			"5, Pineapple, $3.6, 6",
			"6, Mango, $1.89, 4",
			"7, Snickers chocolate bar, $1.8, 20",
			"8, Broccoli, $1.47, 11",
			"9, Washed Potato, $2.98, 7",
			"10, Good-morning cereal, $5.6, 10",
			"11, Rose apple, $4.98, 5",
			"12, Avocado, $4.99, 5",
			"14, Kiwi fruit green, $2.45, 10",
			"15, Rock melon, $7.98, 2",
			"16, Lettuce, $2.99, 12",
			"17, Chocolate block, $3.59, 7"
			]
		self.assertEquals("\n".join(expected_output), output)

	def test_add_to_cart_cannot_add_out_of_stock_product(self):
		pass

	def test_add_to_cart_cannot_add_more_than_available_stock(self):
		pass

	def test_add_to_cart(self):
		pass

	def test_remove_from_cart_cannot_more_than_current_cart(self):
		pass

	def test_remove_from_cart_cannot_remove_product_not_in_cart(self):
		pass

	def test_remove_from_cart(self):
		pass

	def test_clear(self):
		pass

	def checkout(self):
		pass