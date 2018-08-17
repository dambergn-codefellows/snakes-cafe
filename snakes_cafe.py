from textwrap import dedent
from uuid import uuid4
# import pdb; pdb.set_trace()
# type n for next

WIDTH = 80
ORDER_COMPLETE = False
VALID = False
TAX_RATE = float('.096')
TOTAL = float('0')
CATEGORIES = ['appetizers', 'entrees', 'sides', 'drinks', 'desserts']
MENUE = []


def getMenue(file_path):
  '''Parses data from csv file and builds menue dictonarry.
  '''
  parsedCSV = []
  try:
    with open(file_path, 'r') as rf:
      for line in rf:
        new_line = line.replace('\n', ' ').split(',')
        parsedCSV.append(new_line)
  except(FileNotFoundError, TypeError) as e:
    print('file not found')
    
  for dictonary in range(2,len(parsedCSV)):
    MENUE.append(
    {parsedCSV[1][0] : parsedCSV[dictonary][0], 
    parsedCSV[1][1] : parsedCSV[dictonary][1], 
    parsedCSV[1][2] : int(parsedCSV[dictonary][2]), 
    parsedCSV[1][3] : float(parsedCSV[dictonary][3]), 
    parsedCSV[1][4] : int(parsedCSV[dictonary][4]), 
    parsedCSV[1][5] : int(parsedCSV[dictonary][5])})


def greeting():
  # multi line string
  """Function which will greet the user when the application executes for 
  the first time.
  """
  ln_one = 'Welcome to the Snakes Cafe!'
  ln_two = 'Please see our menu below.'
  ln_three = 'To quit at any time, type "quit"'

  print(dedent(f'''
    {'*' * WIDTH}
    {'**' + (' ' * (((WIDTH - 2) - len(ln_one)) // 2)) + ln_one + (' ' * (((WIDTH - 4) - len(ln_one)) // 2)) + '**'}
    {'**' + (' ' * (((WIDTH - 4) - len(ln_two)) // 2)) + ln_two + (' ' * (((WIDTH - 4) - len(ln_two)) // 2)) + '**'}
    {'**' + (' ' * (WIDTH - 4)) + '**'}
    {'**' + (' ' * (((WIDTH - 4) - len(ln_three)) // 2)) + ln_three + (' ' * (((WIDTH - 4) - len(ln_three)) // 2)) + '**'}
    {'*' * WIDTH}
    '''))


def list_category(category):
  """Prints out menue items within a catagory.
  """
  print(dedent(f'''
    {category}
    {'-' * len(category)}'''))
  for menue in MENUE:
    item = menue['item']
    price = "%.2f" % round(float(menue['price']),2)
    space = (' ' * (WIDTH - (len(item) + len(str(price)) + 2)))
    if category == menue['category']:
      print(dedent(f'''{item + space + ' $' + str(price)}'''))


def message():
  """Message that prints out after the menue on program start.
  """
  ln_tip = 'Type "help" to see a list of options'
  ln_message = 'Choose if you would like the "breakfast" or "dinner" menue'
  print(dedent(f'''
    {'*' * WIDTH}
    {'**' + (' ' * (((WIDTH - 2) - len(ln_tip)) // 2)) + ln_tip + (' ' * (((WIDTH - 6) - len(ln_tip)) // 2)) + '**'}
    {'**' + (' ' * (((WIDTH - 2) - len(ln_message)) // 2)) + ln_message + (' ' * (((WIDTH - 6) - len(ln_message)) // 2)) + '**'}
    {'*' * WIDTH}
  '''))


def manual():
  """Prints a help screen to guide a user with possible commands and options.
  """
  ln_zero = 'Manual'
  ln_one = 'Type "menue" to re-print the entire menue.'
  ln_two = 'Type "Category" to bring up a list of category options.'
  ln_three = 'Type the name of the category to see the menue items in that category.'
  ln_four = 'Type the name of the menue item you would like to add to the order.'
  ln_five = 'type "order" to print current order to screen.'
  ln_six = 'If you would like to load a custom csv file type "load" "file_path"'
  ln_seven = 'At any time you can type "quit" or "exit" to stop the application.'

  print(dedent(f'''
    {ln_zero}
    {'-' * len(ln_zero)}
    {ln_one}
    {ln_two}
    {ln_three}
    {ln_four}
    {ln_five}
    {ln_six}
    {ln_seven}
  '''))


def exit():
  """exits the programs and prints a goodbye message.
  """
  print(dedent(f'''
  Thank you for using snakes cafe!
  '''))
  #sys.exit()

def complete():
  """Prints out a recipt for the current order status.
  """
  print(dedent(f'''
  {'_' * WIDTH}
  {'The Snakes Cafe'}
  {"Eatability Counts"}
  {''}
  {'Order: ' + str(uuid4())}
  {'=' * WIDTH}'''))
  subtotal = float('0')
  for menue in MENUE:
    item = menue['item']
    order = menue['order']
    price = str("%.2f" % round(float(menue['order']) * float(menue['price']),2))
    space = (' ' * (WIDTH - (len(item) + len(str(order)) + len(str(price) + '    '))))
    if menue['order'] > 0:
      subtotal = float(price) + subtotal
      print(dedent(f'''{item + ' x' + str(order) + space + ' $' + str(price)}'''))
  sales_tax = float(subtotal) * TAX_RATE
  total_due = float(subtotal) + float(sales_tax)
  print(dedent(f'''
  {'*' * WIDTH}
  {'Subtotal: ' + (' ' * (40 - (len(str(subtotal)) + 12))) + '$' + str("%.2f" % float(subtotal))}
  {'Sales Tax: ' + (' ' * (40 - (len(str(sales_tax)) + 12))) + '$' + str("%.2f" % float(sales_tax))}
  {'=' * 40}
  {'Total Due: ' + (' ' * (40 - (len(str(total_due)) + 12))) + '$' + str("%.2f" % float(total_due))}
  {'_' * WIDTH}
  '''))


def add_menue_item(order, menue):
  """Adds a selected item to the current order and iterates it in the dictonary.
  Prints out current total.
  """
  price = "%.2f" % round(float(menue['price']),2)
  menue['order'] = menue['order'] + 1
  print(menue['order'], 'order(s) of', order, 'at $' + str(price) , ' have been added to your meal.')
  global TOTAL
  TOTAL = float(price) + TOTAL
  print('Current Total W/O tax: $' + str("%.2f" % round(float(TOTAL),2)))


def remove_menue_item(order, menue):
  """Removes a selected item to the current order and iterates it in the dictonary.
  Prints out current total.
  """
  price = "%.2f" % round(float(menue['price']),2)
  menue['order'] = menue['order'] - 1
  print(menue['order'], 'order(s) of', order, 'at $' + str(price) , ' have been removed from your meal.')
  global TOTAL
  TOTAL = TOTAL - float(price)
  print('Current Total W/O tax: $' + str("%.2f" % round(float(TOTAL),2)))


def select_menue(order):
  '''Selects which menue to use and prints it to the screen.
  '''
  getMenue(order)
  print_menue()


def print_menue():
  '''Prints out the entire menue to screen.
  '''
  for key in CATEGORIES:
      list_category(key)


def load_custom_menue(file_path):
  del MENUE[:]
  getMenue(file_path)
  print_menue()


def run():
  """Main function to check and pass user input.
  """
  greeting()
  message()
  while ORDER_COMPLETE == False:
    global VALID
    VALID = False
    order = input().lower()
    if order == 'quit' or order == 'exit':
      exit()
      return
    elif (len(MENUE) == 0 and order == "") or (order == 'breakfast' or order == 'dinner'):
      if order == "":
        order = 'dinner'
      VALID = True
      select_menue('./assets/menue_' + order + '.csv')
    elif order == 'man' or order == 'help':
      VALID = True
      manual()
    elif order.split(' ', 1)[0] == 'load':
      VALID = True
      order = order.split(' ', 1)[1]
      load_custom_menue(order)
    elif order == 'category':
      VALID = True
      print('-' * len(order))
      for key in CATEGORIES:
        print(key)
    elif order == 'menue':
      VALID = True
      print_menue()
    for menue in MENUE:
      if order == menue['category']:
        list_category(order)
        print('')
        VALID = True
        break
    for menue in MENUE:
      if order == menue['item']:
        VALID = True
        add_menue_item(order, menue)
    if order.split(' ', 1)[0] == 'remove':
      order = order.split(' ', 1)[1]
      for menue in MENUE:
        if order == menue['item']:
          VALID = True
          remove_menue_item(order, menue)
    if order == 'order':
      VALID = True
      complete()
      continue
    if VALID is False or order == "":
      print('That is not a valid selection please type "help" to see options.')
    else:
      next


if __name__ == '__main__':
  try:
    run()
  except KeyboardInterrupt:
    exit()