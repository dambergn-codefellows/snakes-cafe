from textwrap import dedent


WIDTH = 40
BANK = [
  {
    'item': 'wings',
    'ammount': 6,
    'price': 3,
    'order': 0,
  },
  {
    'item': 'cookies',
    'ammount': 3,
    'price': 1.5,
    'order': 0,
  },
  {
    'item': 'spring rolls',
    'ammount': 4,
    'price': 2,
    'order': 0,
  },
  {
    'item': 'salmon',
    'ammount': 1,
    'price': 15,
    'order': 0,
  },
  {
    'item': 'steak',
    'ammount': 1,
    'price': 18,
    'order': 0,
  },
  {
    'item': 'meat tornado',
    'ammount': 1,
    'price': 13,
    'order': 0,
  },
  {
    'item': 'a little garden',
    'ammount': 1,
    'price': 3.5,
    'order': 0,
  },
  {
    'item': 'ice cream',
    'ammount': 1,
    'price': 2.5,
    'order': 0,
  },
  {
    'item': 'cake',
    'ammount': 1,
    'price': 2.5,
    'order': 0,
  },
  {
    'item': 'pie',
    'ammount': 1,
    'price': 2.5,
    'order': 0,
  },
  {
    'item': 'coffee',
    'ammount': 1,
    'price': .75,
    'order': 0,
  },
  {
    'item': 'tea',
    'ammount': 1,
    'price': .75,
    'order': 0,
  },
  {
    'item': 'blood of the innocent',
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


def run():
  greeting()
  Appetizers()
  Entrees()
  Desserts()
  Drinks()
  Message()
  # for item in BANK:
  #   user_input = ask_question(item['question'])
  #   status = check_input(user_input, item)
  #   feedback(status)


if __name__ == '__main__':
  run()