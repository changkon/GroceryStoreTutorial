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
		self.grocery_store = GroceryStoreMain.initialise_store()
		self.user = GroceryStoreMain.initialise_user()

	def test_user_name(self):
		self.assertEqual("May Lin Tye", self.user.name)

	def test_product_print(self):
		# GIVEN
		bread = self.grocery_store.get_product(1)

		# WHEN
		with capture() as (out, err):
			bread.print()

		output = out.getvalue().strip()
		expected_output = "1, Fresh toast bread white, $3.99, 20"
		# THEN
		self.assertEqual(expected_output, output)

	def test_grocery_store_print_initial_products(self):
		# WHEN
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
		# THEN
		self.assertEqual("\n".join(expected_output), output)

	def test_grocery_store_print_products_does_not_print_out_of_stock_products(self):
		# GIVEN
		# update products
		garlic = self.grocery_store.get_product(4)
		garlic.quantity = 0
		chocolate = self.grocery_store.get_product(17)
		chocolate.quantity = 7
		banana = self.grocery_store.get_product(13)
		banana.quantity = 0

		# WHEN
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
		# THEN
		self.assertEqual("\n".join(expected_output), output)

	def test_add_to_cart_cannot_add_out_of_stock_product(self):
		# GIVEN
		bread = self.grocery_store.get_product(1)
		bread.quantity = 0

		# WHEN
		with capture() as (out, err):
			self.user.add_to_cart(bread, 1)

		output = out.getvalue().strip()
		expected_output = "Sorry, item 1 is out of stock. Please select a different item"
		# THEN
		self.assertEqual(expected_output, output)

	def test_add_to_cart_cannot_add_more_than_available_stock(self):
		# GIVEN
		bread = self.grocery_store.get_product(1)
		# WHEN
		with capture() as (out, err):
			self.user.add_to_cart(bread, bread.quantity + 1)

		output = out.getvalue().strip()
		expected_output = "Cannot add more than what is available in stock"

		# THEN
		self.assertEqual(expected_output, output)

	def test_add_to_cart(self):
		# GIVEN
		bread = self.grocery_store.get_product(1)
		milk = self.grocery_store.get_product(2)

		# WHEN
		with capture() as (out, err):
			self.user.add_to_cart(bread, 1)
			self.user.add_to_cart(milk, 5)

		output = out.getvalue().strip()
		expected_output = "1 Fresh toast bread white is added to the shopping cart\n5 Low-fat milk is added to the shopping cart"
		# THEN
		self.assertEqual(expected_output, output)
		self.assertEqual(2, len(self.user.cart.items()))
		self.assertEqual(1, self.user.cart.get(bread))
		self.assertEqual(5, self.user.cart.get(milk))

	def test_remove_from_cart_cannot_more_than_current_cart(self):
		# GIVEN
		potato = self.grocery_store.get_product(10)
		cart = {
			potato: 3
		}
		self.user.cart = cart

		# WHEN
		with capture() as (out, err):
			self.user.remove_from_cart(potato, 5)

		output = out.getvalue().strip()
		expected_output = "Cannot remove more than what is in the cart"
		# THEN
		self.assertEqual(expected_output, output)

	def test_remove_from_cart_cannot_remove_product_not_in_cart(self):
		# WHEN
		with capture() as (out, err):
			self.user.remove_from_cart(self.grocery_store.get_product(1), 1)

		output = out.getvalue().strip()
		expected_output = "This item is not in the shopping cart"
		# THEN
		self.assertEqual(expected_output, output)

	def test_remove_from_cart(self):
		# GIVEN
		chocolate = self.grocery_store.get_product(17)
		lettuce = self.grocery_store.get_product(16)
		cart = {
			chocolate: 2,
			lettuce: 4
		}
		self.user.cart = cart

		# WHEN
		with capture() as (out, err):
			self.user.remove_from_cart(chocolate, 2)
			self.user.remove_from_cart(lettuce, 3)

		output = out.getvalue().strip()
		expected_output = "2 Chocolate block is removed from the shopping cart\n3 Lettuce is removed from the shopping cart"
		# THEN
		self.assertEqual(expected_output, output)

	def test_clear(self):
		# GIVEN
		milk = self.grocery_store.get_product(2)
		broccoli = self.grocery_store.get_product(8)
		cart = {
			milk: 7,
			broccoli: 4
		}
		self.user.cart = cart
		self.assertEqual(2, len(self.user.cart))

		# WHEN
		with capture() as (out, err):
			self.user.clear()

		output = out.getvalue().strip()
		expected_output = "All items are cleared from the shopping cart"
		# THEN
		self.assertEqual(expected_output, output)
		self.assertEqual({}, self.user.cart)

	def test_clear_on_empty_cart(self):
		# GIVEN
		self.assertEqual({}, self.user.cart)

		# WHEN
		with capture() as (out, err):
			self.user.clear()

		output = out.getvalue().strip()
		expected_output = "All items are cleared from the shopping cart"
		# THEN
		self.assertEqual(expected_output, output)

	def test_checkout_is_insufficient(self):
		# GIVEN
		self.assertEqual({}, self.user.cart)
		bread = self.grocery_store.get_product(1)
		garlic = self.grocery_store.get_product(4)
		cart = {
			bread: 13,
			garlic: 5
		}
		self.user.cart = cart
		result = None
		# WHEN
		with capture() as (out, err):
			result = self.user.checkout()

		required_amount = bread.price * 13 + garlic.price * 5
		output = out.getvalue().strip()
		expected_output = "Insufficient funds to purchase item(s)\n${} required to purchase but current balance is ${}".format(round(required_amount, 2), self.user.balance)
		# THEN
		self.assertEqual(expected_output, output)
		self.assertEqual(False, result)

	def test_checkout_prints_bill_on_empty_cart(self):
		# GIVEN
		result = None
		# WHEN
		with capture() as (out, err):
			result = self.user.checkout()

		output = out.getvalue().strip()
		expected_output = "Cannot checkout empty cart"
		# THEN
		self.assertEqual(expected_output, output)
		self.assertEqual(False, result)

	def test_checkout(self):
		# GIVEN
		bread = self.grocery_store.get_product(1)
		garlic = self.grocery_store.get_product(4)
		broccoli = self.grocery_store.get_product(8)
		chocolate = self.grocery_store.get_product(17)
		cart = {
			chocolate: 2,
			bread: 5,
			broccoli: 3,
			garlic: 1
		}
		self.user.cart = cart
		self.assertEquals(4, len(self.user.cart.items()))
		result = None

		# WHEN
		with capture() as (out, err):
			result = self.user.checkout()

		output = out.getvalue().strip()
		expected_output = "Checking out items ...\nFresh toast bread white/5/$19.95\nFresh garlic/1/$1.98\nBroccoli/3/$4.41\nChocolate block/2/$7.18\nTotal amount due: $33.52"
		# THEN
		self.assertEquals(0, len(self.user.cart.items()))
		self.assertEqual(expected_output, output)
		self.assertEqual(True, result)