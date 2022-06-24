"""
use this in terminal: python3 code-along.py
"""

# Intro (after un-commenting code below, fix the indentation or code wont run)
        
        # The quick brown fox jumped
        # T => 0 (the first element has an index of 0)
        # h => 1
        # e => 2
        # ' ' => 3

        # starter_sentence = 'The quick brown fox jumped'

        # new_sentence = 'Thy ' + starter_sentence[4:]
        # print(new_sentence) 

# Heredoc / repr (after un-commenting code below, fix the indentation or code wont run)

        # content = """
        # Nullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo. 

        # Vestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in. 

        # Integer posuere erat a ante venenatis dapibus posuere velit aliquet.
        # """.strip()

        # # print(repr(content))

        # long_string = '\nNullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.\n\nVestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.\n\nInteger posuere erat a ante venenatis dapibus posuere velit aliquet.\n'

        # print(long_string)

# string interpolation in Python (after un-commenting code below, fix the indentation or code wont run)

        # name = 'Parker'
        # product = 'Python elearning course'

        # email_content = f"""
        # Hi {name}

        # Thank you for purchasing {product}

        # Regards,

        # Sales Team
        # """
        # print (email_content)

# tuples (after un-commenting code below, fix the indentation or code wont run)

        # name = 'Parker'
        # age = 20
        # product = 'Python Elearning Course'

        # greeting = "Hi {0}, you are listed as {1} years old and you have purchased {2}...".format(name, age, product)

        # print (greeting)

# how to use if and in (after un-commenting code below, fix the indentation or code wont run)

        # sentence = 'The quick brown fox jumps over the lazy dog'

        # query = sentence.find('oops')
        # query_two = sentence.index('oops')

        # print (query)
        # print (query_two)

        # query = 'jumps' in sentence

        # if 'jumps' in sentence:
        #     print('Hello There')

# Replace function (after un-commenting code below, fix the indentation or code wont run)

        # sentence = 'The quick brown fox jumps over the lazy dog'

        # sentence = sentence.replace('quick', 'slow')
        # sentence = sentence.replace('brown', 'black')

        # print (sentence)

# Negative Index Values (after un-commenting code below, fix the indentation or code wont run)

        # sentence = 'The quick brown fox jumps over the lazy dog.'

        # print (sentence[-4:]) 

# strip, lstrip, rstrip functions (after un-commenting code below, fix the indentation or code wont run)

        # url = 'https://google.com'
        # url = url.lstrip('https://')
        # url = url.rstrip('.com')
        # url = url.capitalize()

        # print(url)

# Partition Function (after un-commenting code below, fix the indentation or code wont run)

        # heading = "Python: An Introduction, and Python: Advanced"

        # header, _, subheader = heading.partition(': ')

        # print (header)
        # print (subheader) 

# Split Function (after un-commenting code below, fix the indentation or code wont run)

        # # # heading = "Python: An Introduction, and Python: Advanced"

        # # # header, _, subheader = heading.partition(': ')

        # # # print (header)
        # # # print (subheader)

        # # # tags = 'python,coding,programming,development'

        # # # list_of_tags = tags.split(',')

        # # # print (list_of_tags) 

        # # # list_of_tags = tags.split()

        # # # print (list_of_tags)

        # heading = "Python: An Introduction"

        # heading_list = heading.split(': ')

        # print (heading_list)

# API's (after un-commenting code below, fix the indentation or code wont run)

        # api_data = '5'
        # greeting = 'Hello There'

        # # print (api_data.isalpha())
        # # print (greeting.isalpha())

        # print (api_data.isnumeric())
        # print (greeting.isnumeric())

#  (after un-commenting code below, fix the indentation or code wont run)

        # product_id = 123
        # sale_price = 14.99
        # tip_percentage = 1/5
        # new_product = 150

        # # print(sale_price + new_product) 

        # print(product_id + new_product) 

# Mathematical Operations (after un-commenting code below, fix the indentation or code wont run)
        # print ('Addition')
        # print (100 + 42)

        # print ('- - -')

        # print ('Subtraction')
        # print (100 -42)

        # print ('- - -')

        # print ('Division')
        # print (100 / 42)

        # print ('- - -')

        # print ('Floor Division')
        # print (100 // 42)

        # print ('- - -')

        # print ('Multiplication')
        # print (100 * 42)

        # print ('- - -')

        # print ('Modulus')
        # print (25 % 2)
        # print (2 % 2)
        # print (100 % 42)


        # print ('- - -')

        # print ('Exponents')
        # print (25 ** 2)

# Order of Operations in Python Calculations (after un-commenting code below, fix the indentation or code wont run)

        # Calculation = 8 + 2 * 5 - (9+2) ** 2

        # print (Calculation)

        # """
        # P - Parentheses -> ()
        # E - Exponents -> **
        # M - Multiplication -> *
        # D - Division -> /
        # A - Addition -> +
        # S - Subtraction -> -

        # 8 + 2 * 5 - (9+2) ** 2
        # 8 + 2 * 5 - 11 ** 2
        # 8 + 2 * 5 - 121
        # 8 + 10 - 121
        # 18 - 121
        # -103
        # """

# Assignment Operator (after un-commenting code below, fix the indentation or code wont run)

        # total = 100

        # # total += 10
        # # total -= 10
        # # total *= 2
        # # total /= 10
        # # total **= 2
        # # total //= 10
        # # total %= 10

        # product_two = 120
        # product_three = 10

        # total += product_two
        # total += product_three
        # print (total) 

# Decimal vs Float (after un-commenting code below, fix the indentation or code wont run)

        # # when dealing with financial, scientific, or situations where precision is of great value, import Decimal

        # from decimal import Decimal

        # # product_cost = 88.40
        # # commission_rate = 0.08
        # # qty = 450

        # # product_cost += (commission_rate * product_cost)
        # # print (product_cost * qty) # 42962.4

        # product_cost = Decimal(88.40)
        # commission_rate = Decimal(0.08)
        # qty = 450

        # product_cost += (commission_rate * product_cost)
        # print (product_cost * qty) # 42962.40000000000282883716451

# How to Convert Between the Integer, Float, Decimal and Complex Numeric Data Types in Python (after un-commenting code below, fix the indentation or code wont run)

        # import math

        # loss = -20.25
        # product_cost = 89.99

        # print ('Absolute')
        # print (abs(loss))
        # print('Floor')
        # print (math.floor(product_cost))
        # print('Ceiling')
        # print (math.ceil(product_cost))
        # print('Floor + Absolute')
        # print (math.floor(abs(loss)))
        # print('Round')
        # print (abs(round(product_cost)))
        # print('Square Root')
        # print (math.sqrt(product_cost))
        # print('Another way of doing sqrt')
        # print (math.pow(5, 2))

# Overview of Lists in Python (after un-commenting code below, fix the indentation or code wont run)

        # """
        # User Database Query
        # Anakin
        # Luke
        # Leia
        # """

        # users = ['Anakin', 'Luke', 'Leia']

        # print (users)

        # users.insert (1, 'Padme')

        # print (users)

        # users.append('Ben')

        # print (users)

        # print ([users[4]]) 

        # users[4] = 'Kylo'

        # print (users)

# Three Ways to Remove Elements from a Python List (after un-commenting code below, fix the indentation or code wont run)

        # users = ['Anakin', 'Padme', 'Luke', 'Leia']

        # print (users)

        # users.remove('Leia')

        # print (users)

        # popped_user = users.pop()

        # print (popped_user)
        # print (users) 

        # del users[1]

        # print (users)

# Nested Lists and Best Practices for Storing Multiple Data Types in a Python List (after un-commenting code below, fix the indentation or code wont run)

        # users = ['Anakin', 'Padme', 'Luke', 'Leia']

        # ids = [1, 2, 3, 4]

        # mixed_list = [42, 1.3, 'Chosen One', users]

        # print (mixed_list)

        # user_list = mixed_list.pop()

        # print (user_list)
        # print (mixed_list)

# Python List Query Processes (after un-commenting code below, fix the indentation or code wont run)

        # tags = ['pyton', 'development', 'tutorials', 'code']

        # number_of_tags = len(tags)
        # last_item = tags[-1]
        # index_of_last_item = tags.index(last_item)

        # print (number_of_tags)
        # print (last_item)
        # print (index_of_last_item) 

# How to Sort Lists in Python (after un-commenting code below, fix the indentation or code wont run)

        # tags = ['pyton', 'development', 'tutorials', 'code']

        # print (tags)

        # tags.sort()

        # print (tags)

        # tags.sort (reverse = True)

        # print (tags)

        # totals = [234, 1, 543, 2345]

        # totals.sort(reverse = True)

        # print (totals)

# min + max (after un-commenting code below, fix the indentation or code wont run)

        # nums = [1, 3, 10, 66, 55, 42, 78, 99]

        # print (min(nums))
        # print (max(nums))

# Using the join Function in Python to Build a URL Query String (after un-commenting code below, fix the indentation or code wont run)

        # https://www.starwars.com/search?q=Obi+Wan+Kenobi

        # uri = 'https://www.starwars.com/search?q='
        # tags = ['Obi', 'Wan', 'Kenobi']
        # formatted_tags = '+' .join (tags)
        # query_uri = f'{uri}{formatted_tags}'

        # print (query_uri)

# Overview of Ranges in Python Lists (after un-commenting code below, fix the indentation or code wont run)

        # tags = ['Anakin', 'Rex', 'Fives', 'Hevvy']

        # tag_range = tags[:-1]

        # print (tag_range)

# Advanced Techniques for Implementing Ranges and Slices in Python Lists (after un-commenting code below, fix the indentation or code wont run)

        # tags = [
        #     'Anakin',
        #     'Rex',
        #     'Fives', 
        #     'Hevvy',
        #     'Tup',
        #     'Echo',
        #     'Hardcase',
        #     'CutUp',
        #     'DroidBait'
        # ]

        # # # # tag_range = tags[:-1:2]
        # # # # tag_range = tags[::-1]
        # # # tags.sort(reverse=True)
        # # sorted_tags = tags.sort(reverse=True)
        # tags.sort(reverse=True)


        # # # # print (tag_range)
        # # # print(tags)
        # # print (sorted_tags)
        # print (tags)

# Guide to the sorted Function in Python (after un-commenting code below, fix the indentation or code wont run)

        # sales_prices = [
        #         1,
        #         3,
        #         10,
        #         40,
        #         83,
        #         100,
        #         100,
        #         220,
        #         400
        # ]
        # # # # sales_prices.sort()
        # # # sorted_list = sales_prices.sort()
        # # sorted_list = sorted(sales_prices)
        # sorted_list = sorted(sales_prices, reverse = True)

        # # # # print (sales_prices)
        # # # print (sorted_list)
        # # print (sorted_list)
        # print (sorted_list)

# How to Find the Median of a Python List with an Odd Number of Numbers (after un-commenting code below, fix the indentation or code wont run)

        # import math

        # """
        # Tools:
        # - math library
        # - sorted function
        # - list slicing
        # - computations
        # """

        # sale_prices = [
        #   100,
        #   83,
        #   220,
        #   40,
        #   100,
        #   400,
        #   10,
        #   1,
        #   3
        # ]

        # sorted_list = sorted(sale_prices)
        # num_of_sales = len(sorted_list)
        # half_slice = math.floor(num_of_sales/2)
        # first_sale_items = sorted_list[:half_slice]
        # last_sale_items = sorted_list[-(half_slice):]
        # median = sorted_list [math.floor(half_slice):(math.floor(half_slice)+1)]

        # # print (sorted_list[4:5])

        # print (sorted_list)
        # print (first_sale_items)
        # print (median)
        # print (last_sale_items)

# Working with the slice Class in Python to Store Slices (after un-commenting code below, fix the indentation or code wont run)

        # tags = [
        #         'Anakin',
        #         'Rex',
        #         'Fives', 
        #         'Hevvy',
        #         'Tup'
        # ]

        # # print(tags[:2])
        # slice_obj = slice(1 ,4, 2) 

        # print (slice_obj.start) 
        # print (slice_obj.stop) 
        # print (slice_obj.step) 

        # print(tags[slice_obj])

# How to Add to a List in Python with Both In Place and Copy Processes (after un-commenting code below, fix the indentation or code wont run)

        # tags = ['Anakin','Rex','Fives', 'Hevvy','Tup']

        # # nope
        # # tags[-1] = 'wolffe'
        # # tags.extend('Wolffe')
        # # new_tags = tags.extend(['Wolffe'])
        # new_tags = tags + ['Wolffe']

        # print(new_tags)

        # print(tags)

# Overview of Python Dictionaries (after un-commenting code below, fix the indentation or code wont run)

        # troopers = {
        #         "cpt": "Rex",
        #         "arc": "Fives",
        #         "cmdr": "Cody",
        #         "ct": "Hevvy",
        # }

        # arc_trooper = troopers['arc']
        # captain = troopers['cpt']
        # print (arc_trooper)
        # print (captain)

# Guide to Nested Collections in Python Dictionaries (after un-commenting code below, fix the indentation or code wont run)

        # battalions = {
        #     "501st": ["Rex", "Fives", "Echo"],
        #     "212th": ["Cody", "Waxer", "Boil"],
        #     "wolf-pack": ["Wolffe", "Sinker", "Comet"]
        # }

        # print (battalions["501st"])
        # print (battalions["212th"])
        # print (battalions["wolf-pack"])

# How to Add New Key/Value Pairs to Python Dictionaries (after un-commenting code below, fix the indentation or code wont run)

        # battalions = {
        #     "501st": ["Rex", "Fives", "Echo"],
        #     "212th": ["Cody", "Waxer", "Boil"],
        #     "wolf-pack": ["Wolffe", "Sinker", "Comet"]
        # }

        # battalions['Jedi'] = ['Anakin Skywalker', 'Obi-Wan Kenobi']
        # print(battalions)

# Guide to Using the get Function in Python Dictionaries to Configure Fallback Lookup Values (after un-commenting code below, fix the indentation or code wont run)

        # battalions = {
        #     "501st": ["Rex", "Fives", "Echo"],
        #     "212th": ["Cody", "Waxer", "Boil"],
        #     "wolf-pack": ["Wolffe", "Sinker", "Comet"],
        #     "jedi": ["Anakin Skywalker", "Obi-Wan Kenobi"]
        # }

        # featured_battalion = battalions.get('501st', 'No featured battalion')

        # print(featured_battalion)

# Guide to Python Dictionary View Objects (after un-commenting code below, fix the indentation or code wont run)

        # troopers = {
        #     "cpt": "Rex",
        #     "arc": "Fives",
        #     "cmdr": "Cody",
        #     "ct": "Hevvy",
        # }

        # trooper_names = list(troopers.copy().values())

        # battalions = {
        #     "501st": ["Rex", "Fives", "Echo"],
        #     "212th": ["Cody", "Waxer", "Boil"],
        #     "wolf-pack": ["Wolffe", "Sinker", "Comet"],
        #     "task-force-99": ["Hunter", "Crosshair", "tech", "Wrecker", "Omega"]
        # }

        # battalion_grouping = battalions.items()

        # """
        # [
        #     ('501st', ['Rex', 'Fives', 'Echo']), ('212th', ['Cody', 'Waxer', 'Boil']), ('wolf-pack', ['Wolffe', 'Sinker', 'Comet']), ('task-force-99', ['Hunter', 'Crosshair', 'tech', 'Wrecker', 'Omega'])
        # ]
        # """

        # print(list(battalion_grouping)[1])
        # """
        # ('212th', ['Cody', 'Waxer', 'Boil'])
        # """
        # print(list(battalion_grouping)[1][1])
        # """
        # ['Cody', 'Waxer', 'Boil']
        # """
        # print(list(battalion_grouping)[1][1][1])
        # """
        # Waxer
        # """

# Overview of the Multiple Methods for Deleting Items in a Python Dictionary (after un-commenting code below, fix the indentation or code wont run)

        # battalions = {
        #     "501st": ["Rex", "Fives", "Echo"],
        #     "212th": ["Cody", "Waxer", "Boil"],
        #     "wolf-pack": ["Wolffe", "Sinker", "Comet"],
        #     "task-force-99": ["Hunter", "Crosshair", "tech", "Wrecker", "Omega"]
        # }

        # removed_team = battalions.pop('jedi', 'no battalion found')

        # print (battalions)
        # print (removed_team)

# Guide to Working with Lists of Nested Dictionaries (after un-commenting code below, fix the indentation or code wont run)

        # battalions = [
        #     {
        #         '501st': {
        #             'cpt': 'Rex',
        #             'arc': 'Fives',
        #             'ct': 'Hevvy',
        #         }
        #     },
        #     {
        #         '212th': {
        #             'cmdr': 'Cody',
        #             'Jedi': 'Obi-Wan',
        #         }
        #     }
        # ]

        # # print(battalions[0])

        # kenobi = battalions[1].get('212th', 'trooper not found')

        # print(list(kenobi.values())[1])

# Build a Weighted Lottery Function in Python (after un-commenting code below, fix the indentation or code wont run)

        # import numpy as np

        # def weighted_lottery(weights):
        #     container_list = []

        #     for (name, weight) in weights.items():
        #         for _ in range(weight):
        #             container_list.append(name)

        #     return np.random.choice(container_list)

        # weights = {
        #     'winning': 1,
        #     'break_even':2,
        #     'losing':3
        # }

        # print(weighted_lottery(weights))

# Build a Histogram in Python with No 3rd Party Libraries (after un-commenting code below, fix the indentation or code wont run)

        # # # """
        # # # G $$$$$$$$$$$$$$$$$$$
        # # # F $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # # # T $$$$$$$$$$$
        # # # O $$$$$$$$$$$$$
        # # # """

        # # # sales = {
        # # #     'google': 20,
        # # #     'facebook': 42,
        # # #     'twitter': 10,
        # # #     'offline': 12,
        # # # }

        # # # print ('g ' + sales['google'] * '$')
        # # # print ('f ' + sales['facebook'] * '$')
        # # # print ('t ' + sales['twitter'] * '$')
        # # # print ('o ' + sales['offline'] * '$')


        # # sales = {
        # #     'nike': 15,
        # #     'adidas': 7,
        # #     'vans': 12,
        # # }

        # # print ('n ' + sales['nike'] * '$')
        # # print ('a ' + sales['adidas'] * '$')
        # # print ('v ' + sales['vans'] * '$')

        # droids_killed = {
        #     'rex': 72,
        #     'fives': 57,
        #     'hevvy': 103,
        #     'anakin': 19
        # }

        # print ('r ' + droids_killed['rex'] * 'x')
        # print ('f ' + droids_killed['fives'] * 'x')
        # print ('h ' + droids_killed['hevvy'] * 'x')
        # print ('a ' + droids_killed['anakin'] * 'x')

# Introduction to Python Tuples (after un-commenting code below, fix the indentation or code wont run)

        # """
        # List : []
        # Dictionary: {}
        # Tuple: ()
        # """
        # """
        # Tuple: immutable
        # List: mutable
        # """
        # """
        # You cant sort a Tuple. (post.sort)
        # """

        # post = ('Python Basics', 'Intro guide to Python', 'Some cool python content')

        # title, sub_heading, content = post

        # # title = post[0]
        # # sub_heading = post[1]
        # # content = post[2]

        # print (title)
        # print (sub_heading)
        # print (content)

# Working with Lists Nested in Tuples (after un-commenting code below, fix the indentation or code wont run)

        # post = ('Python Basics', 'Intro guide to Python', 'Some cool python content')

        # tags = ['python', 'coding', 'tutorial']

        # post += (tags,)

        # print (post[-1][1])

# Guide to Slices in Python Tuples (after un-commenting code below, fix the indentation or code wont run)

        # post = ('Python Basics', 'Intro guide to Python', 'Some cool python content', 'published')

        # print (post[1::2])

# Three Ways to Remove Elements from a Python Tuple (after un-commenting code below, fix the indentation or code wont run)

        # post = ('Python Basics', 'Intro guide to Python', 'Some cool python content', 'published')

        # # # """
        # # # [ #1 ] : Removing elements from end
        # # # """
        # # # post = post[:-2]

        # # # print (post)

        # # """
        # # [ #2 ] : Removing elements from the beginning
        # # """
        # # post = post[1:]

        # # print (post)

        # """
        # [ #3 ] : Removing specific element (messy / not recommended) - since tuples are immutable, you will need to turn it into a list first, after removing an element you will need to turn it back into a Tuple.
        # """
        # post = list(post)
        # post.remove('published')
        # post = tuple(post)

        # print (post)

# How to Use a Tuple as a Dictionary Key in Python (after un-commenting code below, fix the indentation or code wont run)

        # """
        # Metadata : Often referred to as data that describes other data, metadata is structured reference data that helps to sort and identify attributes of the information it describes.
        # """

        # priority_index = {
        #     (1, 'premier'): [1, 34, 12],
        #     (1, 'mvp'): [84, 22, 24],
        #     (2, 'standard'): [93, 81, 3],
        # }

        # print (list(priority_index.keys()))

# Guide to Python's Zip Function (after un-commenting code below, fix the indentation or code wont run)

        # """
        # If you want to combine two elements, you 
        # can use zip to merge the two.
        # """

        # positions = ['2b', '3b', 'ss', 'dh']
        # players = ['Altuve', 'Bregman', 'Correa', 'Gattis']

        # scoreboard = zip(positions, players)

        # print(list(scoreboard))

# Introduction to the Python Set Data Structure (after un-commenting code below, fix the indentation or code wont run)

        # """
        # What a Set is and how to use it : A set is always going to have unique items, 

        # """

        # tags = {
        #     'python',
        #     'coding',
        #     'tutorials',
        #     'coding'
        # }
        # # Nope
        # # print (tags[0])

        # query_one = 'python' in tags
        # query_two = 'ruby' in tags


        # print (query_one)
        # print (query_two)

# Introduction to Python Loops (after un-commenting code below, fix the indentation or code wont run)

        # """ 
        # while loop : if you dont tell the loop when to stop, it will keep on going, if you dont implement correctly you might come across an infinite loop and the program will crash.
        # for-in loop : will only run as many times as you tell it to. so if you have 50 gum-balls and tell it to run 50 times, it will stop on the last gum-ball.
        # """

# How to Implement Python Loops for Lists, Tuples, and Dictionaries (after un-commenting code below, fix the indentation or code wont run)

        # # players = ('Altuve', 'Bregman', 'Correa', 'Gattis')

        # # for player in players:
        # #     print (player)

        # """ 
        # for Dictionaries
        # """

        # players = {
        #     '2b': 'Altuve',
        #     '3b': 'Bregman',
        #     'ss': 'Correa',
        #     'dh': 'Gattis'
        # }

        # for position, player in players.items():
        #     print('Position: ', position)
        #     print('Player Name: ', player)

# How to Loop Through the Characters of a Python String (after un-commenting code below, fix the indentation or code wont run)

        # alphabet = 'abcdefghijklmnopqrstuvwxyz'

        # for letter in alphabet:
        #     print(letter)

        # print('Now you know your ABC\'S. Next time wont you sing with me!')

# Guide to Looping Over Ranges in Python (after un-commenting code below, fix the indentation or code wont run)

        # """ 
        # range can take 2-3 arguments.

        # 1, 10 : doesnt count up to 10, it'll stop at 
        # 10 so instead will count from 1-9.

        # to skip values : pass in the third argument 
        # in the range. putting in a '2', it will skip 
        # every other value. plugging in a '3' will skip 
        # every third value.
        # """

        # for num in range(1, 10, 2):
        #         print(num)

# Guide to Continue and Break in Python Loops (after un-commenting code below, fix the indentation or code wont run)

    # usernames = [
    #   'jon',
    #   'tyrion',
    #   'theon',
    #   'cersei',
    #   'sansa',
    # ]

    # for username in usernames:
    #     if username ==  'cersei':
    #         print (f'{username} was found at index {usernames.index(username)}')
    #         break
    #     print(username)

    #     # printing out all names and saying theyre all allowed besides Cersei: jon is allowed
    #         # tyrion is allowed
    #         # theon is allowed
    #         # Sorry, cersei, you are not allowed
    #         # sansa is allowed

    #     #     print (f'Sorry, {username}, you are not allowed')
    #     #     continue 
    #     # else:
    #     #     print(f'{username} is allowed')

# Overview of While Loops in Python (after un-commenting code below, fix the indentation or code wont run)

    #     # nums = list(range(1, 100))

    #     # while len(nums) > 0:
    #     #     print (nums.pop())
        
    # def guessing_game():
    #     while True: 
    #         print ('What is your guess')
    #         guess = input()

    #         if guess == '42':
    #             print ('Correct!')
    #             return False
    #         else:
    #             print(f'{guess} is incorrect, please try again.\n')

    # guessing_game()

# How to Combine and Flatten Lists in Python with the For / In Loop (after un-commenting code below, fix the indentation or code wont run)

    # legacy_characters = ['Anakin', 'Kenobi']
    # new_characters = ['Reva', 'Tala']
    # raw_db = [legacy_characters, new_characters]

    # print (raw_db)

    # for x in new_characters:
    #     legacy_characters.append(x)

    # print(legacy_characters)

# Introduction to Using List Comprehension in Python (after un-commenting code below, fix the indentation or code wont run)

    # num_list = range(1, 11)
    # cubed_nums = []

    # # long syntax
    #     # for num in num_list:
    #     #     cubed_nums.append(num ** 3)

    # # short syntax
    #     # cubed_nums = [num ** 3 for num in num_list]

    # # even nuumbers syntax

    #     # even_num = []

    #     # for x in num_list:
    #     #     if x % 2 == 0:
    #     #         even_num.append(x)

    #     # print (even_num)

    # even_numbers = [num for num in num_list if num % 2 == 0]

    # print (even_numbers)

    # # print (list(num_list))
    # # print ('---------------------------------------------')
    # # print (cubed_nums)

# Build an HTML Heading Generator Function in Python (after un-commenting code below, fix the indentation or code wont run)

    # """ 
    # heading_generator(title, heading_type)
    # heading_generator('Greeting', '1')
    # <h1>Greeting</h1>

    # heading_generator('Hello There', '3')
    # <h3>Hello There</h3>
    # """

    # def heading_generator(title, heading_type):
    #     return f'<h{heading_type}>{title}</h{heading_type}>'

    # print (heading_generator('Greeting', '1'))
    # print (heading_generator('Hello There', '3'))


# Overview of Python Conditionals (after un-commenting code below, fix the indentation or code wont run)

    # age = 100

    # if age < 21:
    #     print (f'I\'m sorry {age} is too young to partake of the devils juice.')
    # elif age >= 100:
    #     print (f'{age} is too old to partake, go back to the old folks home.')
    # else:
    #     print (f'Come on in, {age} fits the age requirement to partake of the devils juice.')

# How to Use the Ternary Operator in Python Conditionals (after un-commenting code below, fix the indentation or code wont run)

    # role = 'admin'

    # # one line
    # auth = 'can access' if role == 'admin' else 'cannot access'

    # print (auth)

    # # multi line
    # if role == 'admin':
    #     print ('can access')
    # else:
    #     print ('cannot access')

# Full List of Python Conditional Operators (after un-commenting code below, fix the indentation or code wont run)

    # """
    # List of comparison operators
    # == Equality
    # != Inequality
    # <> Inequality (deprecated)
    # >  Greater than
    # >= Greater than or equal to
    # < Less than
    # <= Less than or equal to
    # """

    # user_list = ['parker', 'ava']
    # second_list = ['mike', 'reagan']

    # if user_list == second_list:
    #     print ('They match.')
    # else:
    #     print ('They do not match.')

# How to Check if a Value is Included in a Python String or List (after un-commenting code below, fix the indentation or code wont run)

    # sentence = 'The quick brown fox jumps over the lazy Dog.'
    # word = 'quick'
    # word_2 = 'dog'

    # if word in sentence:
    #     print ('the word was in the sentence.')
    # else:
    #     print ('the word was not in the sentence.')

    # if word_2.capitalize() in sentence:
    #     print ('the word was in the sentence.')
    # else:
    #     print ('the word was not in the sentence.')

    # nums = [1, 2, 3, 4]

    # if 3 in nums:
    #     print ('the number was found.')
    # else:
    #     print ('the number was not found.')

# How to Build Compound Conditionals in Python (after un-commenting code below, fix the indentation or code wont run)

    # # username = 'pkelliott'
    # # email = 'pk@elliott.com'
    # # password = 'order66'

    # # if (username == 'pkelliott' or email == 'pk@elliott.com') and password == 'order66':
    # #     print('Access Permitted.')
    # # else:
    # #   print('Access Denied.')

    # logged_in = True
    # standard_user = True

    # if logged_in and not standard_user:
    #     print('You \'CAN\' access the admin dashboard.')
    # else:
    #     print('You \'CANNOT\' access the admin dashboard.')

# Basic Syntax for Creating Python Functions (after un-commenting code below, fix the indentation or code wont run)

    # def full_name(first, last):
    #     print(f'{first} {last}')

    # full_name('Parker', 'Nelson')
    # full_name('Michael', 'Nelson')

    # def auth(email, password):
    #     if email == 'pk.elliott11@gmail.com' and password == 'SeCrEt':
    #             print ('Authorized')
    #     else:
    #         print ('Not Authorized')
    # auth('pk.elliott11@gmail.com', 'SeCrEt')

    # def counter(max_value):
    #     for num in range(1, max_value):
    #         print(num)

    # counter(501)

# What Does it Mean to Return a Value from a Python Function? (after un-commenting code below, fix the indentation or code wont run)

    # def full_name(first, last):
    #     return (f'{first} {last}')

    # parker = full_name('Parker', 'Nelson')

    # def greeting(name):
    #     print(f'Hello there {name}!')

    # greeting(parker)

# How to Nest Functions in Parent Functions in Python (after un-commenting code below, fix the indentation or code wont run)

    # def greeting(first, last):
    #     def full_name():
    #         return f'{first} {last}'

    #     print(f'Hello there {full_name()}!')

    # greeting('Parker', 'Nelson')

# Guide to Default Arguments in Python Functions (after un-commenting code below, fix the indentation or code wont run)

    # basically the point of the video is to say that you should not set the default value as a list

    # # def greeting(name = 'Guest User'):
    # #     print(f'Hello there, {name}!')

    # # greeting()
    # # greeting('Parker')

    # def some_function(collection = []):
    #     collection.append(1)
    #     print (id(collection))
    #     return collection

    # print (some_function())

    # # other part of program

    # print(some_function()) # [1]

# How to Utilize Named Function Arguments in Python (after un-commenting code below, fix the indentation or code wont run)

    # def full_name(first, last):
    #     print(f'Hello, {first} {last}')

    # full_name(first = 'Parker', last = 'Nelson')

# Guide to Function Argument Unpacking in Python (after un-commenting code below, fix the indentation or code wont run)

    # def greeting(tod, *args):
    #     print (f"Hi, {' '.join(args)}, I hope you are having a good {tod}.")
    #     # print(args)

    # greeting('morning', 'Parker', 'Nelson')
    # greeting('afternoon', 'Parker', 'E', 'Nelson')

# Overview of Keyword Arguments in Python Functions (after un-commenting code below, fix the indentation or code wont run)

    # def greeting(**kwargs):
    #     if kwargs:
    #         print(f"Hello there, {kwargs['first_name']} {kwargs['last_name']}")
    #     else:
    #         print (f"Hi guest, have a great day!")

    # greeting (first_name = 'Parker', last_name = 'Nelson')

# How to Combine All Argument Types in a Single Python Function (after un-commenting code below, fix the indentation or code wont run)

    # def greeting(time_of_day, *args, **kwargs):
    #     print(f"Hello there {' '.join(args)}, I hope that you are having a great {time_of_day}.")

    #     if kwargs:
    #         print('Your tasks for the day are:')
    #         for key, val in kwargs.items():
    #             print(f"{key} => {val}")

    # greeting(
    #     'Morning',
    #     'Parker', 'Nelson',
    #     first = 'Empty dishwasher.',
    #     second = 'Let the dogs out.',
    #     third = 'Coding exercises.'
    # )

# Guide to Python Lambdas (after un-commenting code below, fix the indentation or code wont run)

    # full_name = lambda first, last: f'{first} {last}'

    # # print(full_name('Parker', 'Nelson'))

    # def greeting(name):
    #     print(f'Hello there {name}')

    # greeting(full_name('Parker', 'Nelson'))

# Project Requirements: Build FizzBuzz in Python (after un-commenting code below, fix the indentation or code wont run)

    # """ 
    # write a program that prints out the numbers from 1-100 but for every multiple of 3, print fizz instead, every multiple of 5 print buzz, and for a multiple of both 3 and 5 print fizzbuzz

    # - Function
    # - Looping
    # - Conditionals
    # - Math operators
    # """

    # def buzz(max_num):
    #     for num in range(1, max_num + 1):
    #         if num % 3 == 0:
    #             print('fizz')
    #         elif num % 5 == 0:
    #             print('buzz')
    #         elif num % 5 == 0 and num % 3 == 0:
    #             print('fizzbuzz')
    #         else:
    #             print(num)

    # buzz(100)

# Build a Dynamic Reducer in Python (after un-commenting code below, fix the indentation or code wont run)
    # """ 
    # dynamic reducer([1, 2, 3], '+') # 6 (the sum of all the values)
    # dynamic reducer([1, 2, 3], '-') # -
    # dynamic reducer([1, 2, 3], '*') # 6
    # dynamic reducer([1, 2, 3], '/') # -
    # """

    # import operator
    # from functools import reduce

    # def dynamic_reducer(my_list, op):
    #     operators = {
    #         "+": operator.add,
    #         "-": operator.sub,
    #         "*": operator.mul,
    #         "/": operator.truediv,
    #     }
    #     return reduce((lambda total, element: operators[op](total, element)), my_list)

    # # print(reduce(lambda x, y: x+y, my_list))
    # # print(reduce(lambda x, y: x-y, my_list))
    # # print(reduce(lambda x, y: x*y, my_list))
    # # print(reduce(lambda x, y: x/y, my_list))

    # print(dynamic_reducer([1, 2, 3], '+'))
    # print(dynamic_reducer([11, 12, 13], '-'))
    # print(dynamic_reducer([21, 22, 23], '*'))
    # print(dynamic_reducer([31, 32, 33], '/'))

# Manual Exponent (after un-commenting code below, fix the indentation or code wont run)
        # """ 
        # manual exponent(2, 3) => 8
        # manual exponent(10, 2) => 100
        # """
        # from functools import reduce

        # def manual_exponent(my_list, num):
        #     for num in my_list: x ** y 

        # my_list = [3, 7]

        # print(reduce(lambda x,y: x ** y, my_list))

# Remove the First and Last Element from a Python List (after un-commenting code below, fix the indentation or code wont run)

    # """ 
    # remove_first_and_last(list_to_clean)

    # html = ['<h1>', 'some_content', '</h1>']

    # remove_first_and_last(html)
    # => ['some content']

    # html_2 = ['<h1>', 'some_content', 'more', '</h1>']

    # remove_first_and_last(html_2)
    # => ['some content', 'more']
    # """

    # # one, *two, three = [1, 2, 3]


    # def remove_first_and_last(list_to_clean):
    #     _, *content, _ = list_to_clean
    #     return content

    # html_2 = ['<h1>', 'some_content', 'more', '</h1>']
    # print(remove_first_and_last(html_2))

# Overview of Dunder Methods in Python: __str__ , __init__ , __repr__(after un-commenting code below, fix the indentation or code wont run)

    # class Invoice:

    #     def __init__(self, client, total):
    #         self.client = client
    #         self.total = total
    #     def __str__(self):
    #         return f'Invoice from {self.client} for {self.total}'
    #     def __repr__(self):
    #         return f'Invoice <value: client: {self.client}, total: {self.total}>'

    # inv = Invoice('google', 500)
    # print(str(inv))
    # print(repr(inv))

# How to Build a Custom Iterator Class in Python (after un-commenting code below, fix the indentation or code wont run)

""" 
An Iterator will give you complete control to navigate through the list.
"""
class Lineup:
    def __init__(self, players):
        self.players = players
        self.last_player_index = (len(self.players) - 1)

    def __iter__(self):
        self.n = 0
        return self

    def get_player(self, n):
        return self.players[n]

    def __next__(self):
        if self.n < self.last_player_index:
            player = self.get_player(self.n)
            self.n += 1
            return player
        elif self.n == self.last_player_index:
            player = self.get_player(self.n)
            self.n = 0
            return player

astros = [
    'Springer',
    'Bregman',
    'Altuve',
    'Correa',
    'Reddick',
    'Gonzalez',
    'McCann',
    'Davis',
    'Tucker'
]

astros_lineup = Lineup(astros)
process = iter(astros_lineup)

print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))


#  (after un-commenting code below, fix the indentation or code wont run)

#  (after un-commenting code below, fix the indentation or code wont run)

#  (after un-commenting code below, fix the indentation or code wont run)

#  (after un-commenting code below, fix the indentation or code wont run)

#  (after un-commenting code below, fix the indentation or code wont run)

#  (after un-commenting code below, fix the indentation or code wont run)

#  (after un-commenting code below, fix the indentation or code wont run)

#  (after un-commenting code below, fix the indentation or code wont run)

#  (after un-commenting code below, fix the indentation or code wont run)

#  (after un-commenting code below, fix the indentation or code wont run)

#  (after un-commenting code below, fix the indentation or code wont run)

#  (after un-commenting code below, fix the indentation or code wont run)

#  (after un-commenting code below, fix the indentation or code wont run)

#  (after un-commenting code below, fix the indentation or code wont run)

#  (after un-commenting code below, fix the indentation or code wont run)
