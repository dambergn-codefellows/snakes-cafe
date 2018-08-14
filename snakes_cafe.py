from textwrap import dedent


WIDTH = 40
ORDER_COMPLETE = False
BANK = [
  {
    'item': 'Wings',
    'ammount': 6,
    'price': 3,
    'order': 0,
  },
  {
    'item': 'Cookies',
    'ammount': 3,
    'price': 1.5,
    'order': 0,
  },
  {
    'item': 'Spring Rolls',
    'ammount': 4,
    'price': 2,
    'order': 0,
  },
  {
    'item': 'Salmon',
    'ammount': 1,
    'price': 15,
    'order': 0,
  },
  {
    'item': 'Steak',
    'ammount': 1,
    'price': 18,
    'order': 0,
  },
  {
    'item': 'Meat Tornado',
    'ammount': 1,
    'price': 13,
    'order': 0,
  },
  {
    'item': 'A Little Garden',
    'ammount': 1,
    'price': 3.5,
    'order': 0,
  },
  {
    'item': 'Ice Cream',
    'ammount': 1,
    'price': 2.5,
    'order': 0,
  },
  {
    'item': 'Cake',
    'ammount': 1,
    'price': 2.5,
    'order': 0,
  },
  {
    'item': 'Pie',
    'ammount': 1,
    'price': 2.5,
    'order': 0,
  },
  {
    'item': 'Coffee',
    'ammount': 1,
    'price': .75,
    'order': 0,
  },
  {
    'item': 'Tea',
    'ammount': 1,
    'price': .75,
    'order': 0,
  },
  {
    'item': 'Blood of the Innocent',
    'ammount': 1,
    'price': 100000,
    'order': 0,
  },
]


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


def Appetizers():
  ln_category = 'Appetizers'
  ln_one = 'Wings'
  ln_two = 'Cookies'
  ln_three = 'Spring Rolls'

  print(dedent(f'''
    {ln_category}
    {'-' * len(ln_category)}
    {ln_one}
    {ln_two}
    {ln_three}
    {''}
  '''))


def Entrees():
  ln_category = 'Entrees'
  ln_one = 'Salmon'
  ln_two = 'Steak'
  ln_three = 'Meat Tornado'
  ln_four = 'A Literal Garden'

  print(dedent(f'''
    {ln_category}
    {'-' * len(ln_category)}
    {ln_one}
    {ln_two}
    {ln_three}
    {ln_four}
    {''}
  '''))


def Desserts():
  ln_category = 'Desserts'
  ln_one = 'Ice Cream'
  ln_two = 'Cake'
  ln_three = 'Pie'

  print(dedent(f'''
    {ln_category}
    {'-' * len(ln_category)}
    {ln_one}
    {ln_two}
    {ln_three}
    {''}
  '''))

def Drinks():
  ln_category = 'Drinks'
  ln_one = 'Coffee'
  ln_two = 'Tea'
  ln_three = 'Blood of the Innocent'

  print(dedent(f'''
    {ln_category}
    {'-' * len(ln_category)}
    {ln_one}
    {ln_two}
    {ln_three}
    {''}
  '''))


def Message():
  ln_message = 'What would you like to order?'
  print(dedent(f'''
    {'*' * WIDTH}
    {'**' + (' ' * (((WIDTH - 2) - len(ln_message)) // 2)) + ln_message + (' ' * (((WIDTH - 4) - len(ln_message)) // 2)) + '**'}
    {'*' * WIDTH}
  '''))


def Manual():
  ln_zero = 'Manual'
  ln_one = 'Type "Category" to bring up a list of category options.'
  ln_two = 'Type the name of the category to see the menue items in that category.'
  ln_three = 'Type the name of the menue item you would like to add to the order.'
  ln_four = 'At any time you can type "quit" or "exit" to stop the application.'

  print(dedent(f'''
    {ln_zero}
    {'-' * len(ln_zero)}
    {ln_one}
    {ln_two}
    {ln_three}
    {ln_four}
  '''))


def Category():
  ln_zero = 'Categories'
  ln_one = 'Appetizers'
  ln_two = 'Entrees'
  ln_three = 'Desserts'
  ln_four = 'Drinks'

  print(dedent(f'''
    {ln_zero}
    {'-' * len(ln_zero)}
    {ln_one}
    {ln_two}
    {ln_three}
    {ln_four}
  '''))


def exit():
  print(dedent(f'''
  Thank you for using snakes cafe!
  '''))
  #sys.exit()

#def complete():


def run():
  greeting()
  Appetizers()
  Entrees()
  Desserts()
  Drinks()
  Message()
  while ORDER_COMPLETE == False:
    order = input()
    if order == 'quit' or order == 'exit':
      exit()
      return
    elif order == 'man' or order == 'Man' or order == 'help':
      Manual()
    elif order == 'Category':
      Category()
    elif order == 'Appetizers':
      Appetizers()
    elif order == 'Entrees':
      Entrees()
    elif order == 'Desserts':
      Desserts()
    elif order == 'Drinks':
      Drinks()
    for menue in BANK:
      if order == menue['item']:
        menue['order'] = menue['order'] + 1
        print(menue['order'], 'order(s) of', order, 'have been added to your meal.')
      else:
        next


if __name__ == '__main__':
  run()