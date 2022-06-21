"""
List : []
Dictionary: {}
Tuple: ()
"""

# 1 : Exercise given by Trenton

        # names_one = ('Parker', 'Ava', 'Reagan', 'Mike')

        # names_two = []

        # for name in names_one:
        #     names_two.append(name)

        # print (names_two)

# 2 : Exercise given by Trenton

        # army = {
        #     'legion' : ['501st', '212th', 'wolf-pack'],

        #     'title' : ['captain', 'commando','commander'],

        #     'name' : ['Rex', 'Gregor', 'Wolffe']
        # }

        # army_two = []
        # for x in army.values():
        #     army_two.append(x)
        # print (army_two)

        # army_two = []
        # for x in army.values():
        #     army_two.append(x[0])
        # print (army_two)

        # army_two = []
        # for x in army.values():
        #     army_two.append(x[1])
        # print (army_two)

        # army_two = []
        # for x in army.values():
        #     army_two.append(x[2])
        # print (army_two)

# 3 : Exercise given by Trenton

    # """ 
    # Exercise 1
    # """

        # student = {
            # "name": ["Parker"],
            # "age": [20],
            # "major": ["Web Development"],
            # "year": [2022],
            # "gpa": [4.0],
        # }

    # """ 
    # Exercise 2
    # """
        # student = {
            # "name": ["Parker"],
            # "age": [20],
            # "major": ["Web Development"],
            # "year": [2022],
            # "gpa": [4.0],
        # }
        # featured_student = student.get('name', 'No featured student')

        # print (featured_student)

    # """ 
    # Exercise 3
    # """

        # student = {
            # "name": ["Parker"],
            # "age": [20],
            # "major": ["Web Development"],
            # "year": [2022],
            # "gpa": [4.0],
        # }

        # removed_item = student.pop('year')

        # print (list(student))

    # """ 
    # Exercise 4
    # """

        # student = {
            # "name": ["Parker"],
            # "age": [20],
            # "major": ["Web Development"],
            # "year": [2022],
            # "gpa": [4.0],
        # }

        # student["gpa"] = ['3.9']

        # print (list(student))

    # """ 
    # Exercise 5
    # """

        # student = {
        #     "name": ["Parker"],
        #     "age": [20],
        #     "major": ["Web Development"],
        #     "year": [2022],
        #     "gpa": [3.0],
        # }

        # student["gpa"][0] = '4.0'

        # print (student)

    # """ 
    # Exercise 6
    # """

        # collegeStudents = {
        #     "name": ["Parker", "Mike", "Ava"],
        #     "age": [20, 24, 20],
        #     "major": ["Web Development", "Computer Science", "Aesthetics"],
        #     "year": [2022, 2022, 2023],
        #     "gpa": [4.0, 4.0, 4.0],
        # }

    # """ 
    # Exercise 7
    # """

        # collegeStudents = {
        #     "name": ["Parker", "Mike", "Ava"],
        #     "age": [20, 24, 20],
        #     "major": ["Web Development", "Computer Science", "Aesthetics"],
        #     "year": [2022, 2022, 2023],
        #     "gpa": [3.0, 4.0, 3.7],
        # }

        # print(min(collegeStudents["gpa"]))
        # print(max(collegeStudents["gpa"]))

# 4 : Exercise given by Trenton

    # """ 
    # Task #1
    # """

        # # # # # # List and Dictionary
        # # # # # Teams = {
        # # # # #     "Thunder": ["Parker", "Kobe", "Noah"],
        # # # # #     "PG": ["Preston", "Kael", "Levi"],
        # # # # #     "Skyridge": ["Trevin", "Braden", "Luke"],
        # # # # # }

        # # # # # Tuple
        # # # # Position = ('Point Guard')

        # # # # Float
        # # # subtotal = 85.66
        # # # tip = subtotal * 0.15
        # # # total = tip + subtotal

        # # # print (total)

        # # # Decimal

        # # from decimal import Decimal

        # # productCost = 499.99
        # # commissionRate = 0.12

        # # pay_per_sale = productCost * 0.12

        # # print (pay_per_sale)

        # # Integer

        # import math

        # subtotal = 15
        # tax =  1
        # total = subtotal + tax

        # print (total)

    # """ 
    # Task 2 
    # """

        # # Round your float up

        # import math

        # subtotal = 66.00
        # tax = subtotal * .015
        # total = subtotal + tax

        # print(round(total))
        # print(math.ceil(total))

    # """ 
    # Task 3
    # """

        # # Get the square root of your float

        # import math

        # subtotal = 66.00
        # tax = subtotal * .015
        # total = subtotal + tax

        # # print(total)

        # print (math.sqrt(total))

    # """ 
    # Task 4
    # """

        # # Select the first element from your dictionary

        # star_wars = {
        #     "troopers": ["Rex", "Fives", "Echo"],
        #     "jedi": ["Anakin Skywalker", "Obi-Wan Kenobi", "Ahsoka Tano"],
        #     "sith": ["Darth Vader", "Kylo Ren", "Darth Maul"],
        # }

        # print (list(star_wars)[0])
        # print (star_wars["troopers"][0:])

    # """ 
    # task 5
    # """

        # # Select the second element from your tuple

        # name = ('Parker', 'Ava', 'Mike')

        # print (name[1])

    # """ 
    # Task 6
    # """

        # # Add an element to the end of your list

        # jedi = ["Anakin", "Obi-Wan", "Ahsoka"]

        # jedi.append("Mace Windu")

        # print (jedi)

    # """ 
    # Task 7
    # """

        # # Replace the first element in your list

        # jedi = ["Anakin", "Obi-Wan", "Ahsoka"]

        # jedi [0] = "Yoda"

        # print (jedi)

    # """ 
    # Task 8
    # """

        # # Sort your list alphabetically

        # jedi = ["Anakin", "Obi-Wan", "Ahsoka"]

        # jedi.sort()

        # print (jedi)

    # """ 
    # Task 9
    # """

        # # Use reassignment to add an element to your tuple

        # jedi = ("Anakin", "Obi-Wan", "Ahsoka")
        # jedi = list(jedi)
        # jedi.append("Yoda")
        # jedi = tuple(jedi)

        # print (jedi)

    # """ 
    # Task 10
    # """

        # # Sort your tuple in alphabetical order

        # jedi = ("Anakin", "Obi-Wan", "Ahsoka")
        # jedi = list(jedi)
        # jedi.sort()
        # jedi = tuple(jedi)

        # print (jedi)

# Self-practice ( Append and Replacements )
    # names = ('Parker', 'Michael', 'Ava')
    # print (names)

    # print ('-------append and replacements-------')

    # names = list(names)
    # names.append('Reagan')
    # names[0] = 'pk'
    # names[1] = 'mike'
    # names[2] = 'oovahv'
    # names[3] = 'O-reagan-O'
    # names = tuple(names)

    # print (names)

# 5 : Exercise given by Trenton

    # Write a program that will print the multiplication table of a specific number. Example: 7, 12, 21, 28, 35...

        # print ('multiplication table of 7')
        # print('--------------------------')

        # num = 7

        # for i in range(1, 11):
        #    print(num, 'x', i, '=', num*i)

        # print()
        # print ('multiplication table of 12')
        # print('---------------------------')

        # value = 11

        # for i in range(1,12):
        #     print(value, 'x', i, '=', value*i)

    # Create a list of integers, pull every other integer from that list out and place it in a new list... 

        # integers = ['3', '5', '11', '16', '17', '20', '23', '27', '30', '35', '42']

        # integer_range = integers[0::2]

        # print (integer_range)

        # # integers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        # # for num in range(0, 11, 2):
        # #     print(num)

    # Use the zip function to merge two lists

        # names = [
        #     'Parker',
        #     'Reagan',
        #     'Michael'
        # ]

        # ages = [
        #     '20',
        #     '17',
        #     '24'
        # ]

        # students = zip(names, ages)

        # print (list(students))

    # Create a list of integers and use a for loop to return the total of all of the numbers in the list. 

        # integers = [
        #     23, 
        #     11, 
        #     12, 
        #     16, 
        #     21, 
        #     17, 
        #     7
        # ]

        # sorted_integers = sorted(integers)
        # num_of_integers = len(sorted_integers)
        # sum_of_integers = sum(integers)
        # print(sum_of_integers)

# self practice

    # num = 15

    # for i in range(1,11):
    #     print(num, 'x', i, '=', num*i)

    # print()
    # print ('-------------------------')
    # print()

    # int = [
    #     15,
    #     25,
    #     5,
    #     84, 
    #     125,
    # ]

    # int_num = len(int)

    # print (int_num, 'integers')

    # int_range = int[0::2]

    # print (int_range)

    # print()
    # print ('-------------------------')
    # print()

    # names = [
    #     'parker',
    #     'ava',
    #     'michael',
    #     'mola',
    #     'reagan',
    #     'dad',
    # ]

    # ages = [
    #     '20',
    #     '20',
    #     '24',
    #     '18',
    #     '17',
    #     '56',
    # ]

    # ppl = zip(names, ages)

    # print (list(ppl))

    # print()
    # print ('-------------------------')
    # print()

    # integers = [
    #     15,
    #     25,
    #     5,
    #     84, 
    #     125,
    # ]
    # sum_integers = sum(integers)

    # print(sum_integers)

# Self-practice : Using while loop to add all the numbers between 1 and 50 to eachother

    # num = 50
    # sum = 0

    # while num > 0:
    #     sum += num
    #     num -= 1
        
    # print("The sum is", sum)

    # numm = 11
    # summ = 0
    # while numm > 0:
    #     summ += numm
    #     numm -= 1

    # print ('The sum is ', summ)

    # nuum = 19
    # suum =0

    # while nuum > 0:
    #     suum += nuum
    #     nuum -= 1

    # print('The sum is ', suum)

    # number = 100
    # sum = 0

    # while number > 0:
    #     sum += number
    #     number -= 1
    # print("Hello There, good work on building out this exercise. The sum is ", sum)

# Print the following pattern using a while loop:
    # """
    # xxxxx
    # xxxx
    # xxx
    # xx
    # x
    # """

# num = 50
# sum = 0

# while num > 0:
#     sum += num
#     num -= 1
# print("the sum is ", sum)



# sports = [
#     'basketball',
#     'soccer',
#     'football',
#     'volleyball'
# ]

# for x in sports:
#     if x == 'basketball':
#         print(f'{x} is the best sport')
#     print (x)



# num_list = range(1, 12)
# sq_num = []

# for x in num_list:
#     sq_num.append(x ** 2)



# print (sq_num)

# x = 56.89

# i = True if x == 56.89 else False

# print (i)



# value = 'priceless'

# iPhone = True if value == '$1200' else False

# print (iPhone)



# name = 'Parker'

# winner = f'{name} is the winner' if name == 'Parker' else '{name} is not the winner'

# print (winner)



# import numpy as np

# def weighted_answers(weights):
#     container = []

#     for (name, weight) in answers.items():
#         for _ in range(answers):
#             container.append(name)

# answers = {
#     'yes': 1,
#     'no': 1,
# }



def sum_two_num(num_one, num_two):
    return num_one + num_two

def total(num_one, num_two):
    print(f'the total is {total}')

total(8, 11)







    