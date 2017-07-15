from Product import Product
from GroceryStore import GroceryStore
from User import User

def initialise_stock():
	stock = []
	stock.append(Product(1, 'Fresh toast bread white', 3.99, 20))
	stock.append(Product(2, 'Low-fat milk', 4.80, 10))
	stock.append(Product(3, 'V-energy drink', 2.75, 10))
	stock.append(Product(4, 'Fresh garlic', 1.98, 5))
	stock.append(Product(5, 'Pineapple', 3.60, 6))
	stock.append(Product(6, 'Mango', 1.89, 4))
	stock.append(Product(7, 'Snickers chocolate bar', 1.80, 20))
	stock.append(Product(8, 'Broccoli', 1.47, 11))
	stock.append(Product(9, 'Washed Potato', 2.98, 7))
	stock.append(Product(10, 'Good-morning cereal', 5.60 ,10))
	stock.append(Product(11, 'Rose apple', 4.98, 5))
	stock.append(Product(12, 'Avocado', 4.99, 5))
	stock.append(Product(13, 'Bananas', 2.96, 4))
	stock.append(Product(14, 'Kiwi fruit green', 2.45, 10))
	stock.append(Product(15, 'Rock melon', 7.98, 2))
	stock.append(Product(16, 'Lettuce', 2.99, 12))
	stock.append(Product(17, 'Chocolate block', 3.59, 10))
	return stock

def initialise():
	name = "OrionStore"
	stock = initialise_stock()
	grocery_store = GroceryStore(name, stock)
	return grocery_store

def start():
	starting_balance = 50
	user_name = "Chang Kon"
	user = User(user_name, starting_balance)
	grocery_store = initialise()

	print("Welcome to " + grocery_store.name)

	while True:
		print("1. Show the list of items on sale")
		print("2. Start to shop online")
		print("3. Exit the system")

		user_input = input("Enter selection: ")

		if user_input == "1":
			grocery_store.print_available_products()
		elif user_input == "2":
			pass
		elif user_input == "3":
			print("Bye")
			break
		else:
			print("Unknown command")

if __name__ == "__main__":
	start()