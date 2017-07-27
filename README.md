# A Simple Grocery Store Program
This assignment description is copied from the COMPSCI 101 assignment. I've attached the pdf for that assignment specification which may be helpful to read.

For this program, you will be tasked to complete the implementation for a **simple grocery store program** written in python. The program is a console application which supports tasks such as:

* Viewing items on sale
* Add/remove items to/from shopping cart
* Checkout cart items

You are provided with the following python files:
Files which require completion have **TODO** comments in the python file and are also mentioned below.

* **GroceryStore.py** - Grocery store file which contain information about the available products. **TODO**
* **GroceryStoreMain.py** - Logic to initialise and startup the program. This file already takes care of control flow of the program. **TODO**
* **Product.py** - Product file which contain information about an item sold at the GroceryStore. **TODO**
* **User.py** - User file which allows products/items to be added/removed from cart. **TODO**
* **TestGroceryStore.py** - Use this test file to verify the correctness of your implemention.

**Currently, the program will not function and requires completion.** Before beginning, it is advised understand all the files and how they interact. The methods have been commented to describe their purpose and the requirements of the tasks are described below.

## Installation
The software requires `python3` to run. If you haven't installed python3 yet, follow the below instructions to get started.

### Mac
[Instructions](http://python-guide-pt-br.readthedocs.io/en/latest/starting/install3/osx/)
### Windows
[Download site](https://www.python.org/downloads/)

## Running the software
All commands are executed on the same directory as the python files in a terminal/command line.
### Grocery store
Run the program using `python3 GroceryStoreMain.py`
After executing the above command, the program should display back the top-level menu:
```
Hello Chang Kon Han
Welcome to OrionStore
1. Show the list of items on sale
2. Start to shop online
3. Exit the system
Enter selection:
```
You can interact with the program through keyboard input. The program will detect invalid inputs and continue asking for correct input.
```
Enter selection: 4
Invalid option, please try again!
```

The overall control flow of the program can be outlined as follows:
* Option one of the top-level menu leads to displaying all the items on sale and then returning to the same top-level menu.
* Option two of the top-level menu leads to the second-level menu;
* Option three of the top-level menu leads to exiting from the program;
* Option one or two of the second-level menu leads to adding or removing an items to or from the shopping cart and then returning to the same second-level menu;
* Option 3 of the second-level menu returns back to the top-level menu after a successful checkout. Otherwise, the display remains at the second-level menu.
* Option 4 of the second-level menu leads to discarding the shopping cart and then returning back to the top-level menu.

```
Hello Chang Kon Han
Welcome to OrionStore
1. Show the list of items on sale
2. Start to shop online
3. Exit the system
Enter selection: 2
1. Add an item to the shopping cart
2. Delete an item from the shopping cart
3. Check out the shopping cart
4. Exit without buying
Enter selection: 1
Enter product id to buy: 1
Enter quantity to purchase: 1
1 Fresh toast bread white is added to the shopping cart
1. Add an item to the shopping cart
2. Delete an item from the shopping cart
3. Check out the shopping cart
4. Exit without buying
Enter selection: 3
Checking out items ...
Fresh toast bread white/1/$3.99
Total amount due: $3.99
1. Show the list of items on sale
2. Start to shop online
3. Exit the system
Enter selection: 3
Thank you for shopping with us!
```

### Unit Tests
Run the unit tests by `python3 -m unittest TestGroceryStore.py -v`

All unit tests should pass for correct implementation of the program.

## Tasks
### Changing user name
Change the `GroceryStoreMain.py` file and edit `user_name` variable inside the `initialise_user` method. Change it to your name `May Lin Tye`.
After changing variable, the display should show at the start.
```
Hello May Lin Tye
Welcome to OrionStore
1. Show the list of items on sale
2. Start to shop online
3. Exit the system
Enter selection:
```
### Print product information
Update the `print` method inside `Product.py`. It should print i.e. display into system output the properties of the product, comma-separated. It should display in the order: id, name, price, quantity. The price is prefixed by the `$` symbol. An example output is:
```
1, Fresh toast bread white, $3.99, 20
```

### Print grocery store stock
Update the `print_available_products` method inside `GroceryStore.py`. It should display **current available i.e. quantity is 1 or greater** products. Each product should show its product information. The products are sorted by its product id. Example:
```
1, Fresh toast bread white, $3.99, 20
2, Low-fat milk, $4.8, 10
3, V-energy drink, $2.75, 10
4, Fresh garlic, $1.98, 5
5, Pineapple, $3.6, 6
6, Mango, $1.89, 4
7, Snickers chocolate bar, $1.8, 20
8, Broccoli, $1.47, 11
9, Washed Potato, $2.98, 7
10, Good-morning cereal, $5.6, 10
11, Rose apple, $4.98, 5
12, Avocado, $4.99, 5
13, Bananas, $2.96, 4
14, Kiwi fruit green, $2.45, 10
15, Rock melon, $7.98, 2
16, Lettuce, $2.99, 12
17, Chocolate block, $3.59, 10
```
### Add to cart
Edit the `add_to_cart` method inside `User.py`
