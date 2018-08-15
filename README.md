# snakes-cafe
snakes-cafe

# Use
- when you start the program will will be greeted and a list of menue items will be presented.
- at any time you can exit the application by typing "quit".
- add a item from the menue to the meal order by typing its name (caps sensitive)
- if you need to see the list of a specific category type the category name and it will re-print on screen. (caps sensitive)
- type man or help to bring up on screen instructions.

# Features
- [X]When run, the program should print an intro message and the menu for the restaurant
- [X]The restaurant’s menu should include appetizers, entrees, desserts, and beverages. At least 3 in each category
- [X]The program should prompt the user for an order
- [X]When a user enters an item, the program should print an acknowledgment of their input
- [X]The program should tell the user how to exit
---NEW features---
- [X]Your menu should get a “Sides” category
- [X]Every menu category should have at least 6 items
- [X]Your menu items should all get prices. Use whatever currency symbol you want, but make sure that the user knows what the prices and currencies are.
- [X]Whenever the user adds an item to their order, they’re notified of the total cost of their order up to that point.
- []If the user types order, their entire order is printed to the console.

```
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Blood of the Innocent

***********************************
** What would you like to order? **
***********************************
```

## Change Log

### 2018-08-14
- Updated README.md file.
- Converted inputs to lowercase.
- Created function to build menue from dictonary.
- Code refactored to use dictonary and list data as templates.
- Sides category and 3 side items added.
- Expanded all categories to 6 items.
- Menue now prints out prices of items.
- When added to order price of item is printed as well as a current total.

### 2018-08-13
- Added menue items to select from to print to screen.
- Added ability to re print individual category and exit.
- Orders append to dictonary and print added item and quantity.
- Fixed bug that causes application to crash if incorrect item is typed.
- Added exit to commands that will exit program.
- Added Category command to show available categories.
- Added Manual / help command.

# Software
- linux
```
  sudo apt-get install python3-pip
  sudo pip install --upgrade pip
  pip install --user pipenv
  sudo -H pip install -U pipenv
  pipenv shell
  pipenv install pytest
  pytest -v
```