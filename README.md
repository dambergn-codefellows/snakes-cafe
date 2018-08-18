# snakes-cafe
snakes-cafe

# Use
- when you start the program will will be greeted and a list of menue items will be presented.
- at any time you can exit the application by typing "quit".
- add a item from the menue to the meal order by typing its name.
- if you need to see the list of a specific category type the category name and it will re-print on screen.
- type "order" to print current order to screen.
- type man or help to bring up on screen instructions.

# Features
- [X]When run, the program should print an intro message and the menu for the restaurant
- [X]The restaurant’s menu should include appetizers, entrees, desserts, and beverages. At least 3 in each category
- [X]The program should prompt the user for an order
- [X]When a user enters an item, the program should print an acknowledgment of their input
- [X]The program should tell the user how to exit
- [X]Your menu should get a “Sides” category
- [X]Every menu category should have at least 6 items
- [X]Your menu items should all get prices. Use whatever currency symbol you want, but make sure that the user knows what the prices and currencies are.
- [X]Whenever the user adds an item to their order, they’re notified of the total cost of their order up to that point.
- [X]If the user types order, their entire order is printed to the console.
- [X]Every order should get a universally unique identifier. Consider using the uuid package
- [X]In the order printout you must include sales tax (9.6% in Seattle as of 2018) in the final total (round up to 2 decimal places)
- [X]In the order printout, all of the costs should be right-justified, and all of the item names should be left-justified
- [X]If the user types menu, the entire menu is printed to the console
- [X]If the user types the name of any of your categories, the items in that category should be printed to the console
- [X]If the user types remove <ITEM NAME>, 1 item of the type <ITEM NAME> should be removed from their order, and their order’s total should be printed to the screen
- [X]All input should be case-insensitive
- [ ]Keep your functions small, concise, and testable.
---NEW features---
- [ ]Every menu category should have at least 9 items
- [X]Add to your snakes-cafe project the option to provide a separate file as a menu with the appropriate help text (see Lecture 01). If this option isn’t used, the menu you’ve been building all week will be used.
- [X]The optional separate menu must be a comma-separated value (.csv) file, where each row includes the menu item’s name (str), category (str), price (float), and quantity (int) referring to the in-stock amount of that item.
- [X]If the provided separate menu file isn’t a CSV file, alert the user with an appropriate error message. Note: the user should never see an actual Python Exception
- [ ]When the user adds an item to their order, they should have the option of providing the quantity as well.
- [ ]If they don’t provide the quantity, a quantity of 1 is assumed.
- [ ]If the quantity they provide is invalid (negative or not a number), alert the user with an appropriate error message
- [ ]If the quantity they provide is beyond whatever is left in stock, alert the user with an appropriate error message.
- [ ]If the user tries to add/remove an item that isn’t on whatever menu has been loaded, alert the user with an appropriate error message
- [ ]If the user tries to remove an item that isn’t a part of their order, alert the user with an appropriate error message
- [ ]No matter what, the user should never see a traceback. Not even for a Keyboard Interrupt.
- [ ]Every bit of functionality that you add should be tested.
- [ ]As a general rule at this time, you should have a test for valid, invalid, and edge case variants for every function that you define. There are exceptions. The exceptions are not the rule.
---NEW New features---
- [ ]Every menu category should have at least 12 items
- [ ]Create an Order class. Whatever means you were using to build orders before, replace them with methods and attributes belonging to this class.
- [ ]Every Order should have a uuid
- [ ]Every Order should have an add_item method that takes an item name and a quantity as arguments. There should be a default value for quantity if none is given.
- [ ]Every Order should have a remove_item method that takes an item name and a quantity as arguments. There should be a default value for quantity if none is given.
- [ ]Every Order should have a display_order() method that prints the user’s current order to the console
- [ ]Every Order should have a print_receipt() method that creates a file containing the text of the user’s full order. The file name should be of the format order-<the uuid>.txt and should have the same output as display_order
- [ ]All of the order input-checking that you used to do will be done by this class
- [ ]The repr of Order instances should look like <Order #ba99d8... | Items: 4 | Total: $754.23>
- [ ]When print() is called on an order instance, the user’s current order is printed as if display_order was called.
- [ ]When len() is called on an order instance, the number of items in the order is returned
- [ ]You may have as many helper methods as you want. However, make sure that any attributes and methods that aren’t intended for public use are prefixed with a - [ ]single underscore
- [ ]All of your methods should be narrow in scope
- [ ]Every bit of functionality that you add should be tested.
- [ ]As a general rule at this time, you should have a test for valid, invalid, and edge case variants for every function that you define. There are exceptions. The exceptions are not the rule.

## Change Log

### 2018-08-16
- Updated all functions with descriptions.
- Added KeyboardInterrupt to handle CTRL+C
- Added quantity to dictionarry.
- Changed quantity to inventory.
- Changes to menue and menue.csv
- Attempted some testing with no sucess.
- Created file.io.py to test csv access and parsing.
- Sucessfully able to add csv parsed data to list.
- Commiting to create new branch.
- Created new branch class-04-objects.
- Sucessfully parsed data from CSV file to list of dictonaries.
- Refactored code in snakes_cafe from BANK to MENUE.
- Menue is now created from CSV file, need to create on start select for breakfast or dinner.
- On start you can now type breakfast or dinner to select which menue to use.
- (BUGG): parsed csv menue does not have intigers, need to fix.
- Fixed CSV parser to accomidate int and float values.
- Menu now defaults to dinner if nothing is selected.
- Added ability for user to manually select and load a csv file.
- Commiting and pushing where I am currently at.

### 2018-08-15
- Got test file linked and working properly.
- Added UUID to recipt.
- Refactored adding and printing of menue item added to order.
- Fixed new bug where after order program would exit.
- Fixed message when user enters something that is not a handled option.
- Fixed capitals in function names.
- If the user types menu, the entire menu is printed to the console.
- Remove item from current order by typing remove and the name of the item.
- Attempted some testing with no positive results.
- New branch 'class-03-robust' to impliment new features and tests.
- Added tip to message line at bottom to bring up the help menue.

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
- Type "order" to view your current order so far.
- Tax rate has a easily changeable variable at top of code.

# Software
- linux
```
  sudo apt-get install python3-pip
  sudo pip install --upgrade pip
  pip install --user pipenv
  sudo -H pip install -U pipenv
  pipenv --three
  pipenv shell
  pipenv install pytest
  pytest -v
  pipenv install uuid

  #to remove env
  pipenv --rm

  #to check pipenv
  pipenv check
```