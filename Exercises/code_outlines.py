# log-in credentials
    # username = 'pkelliott'
    # email = 'pk@elliott.com'
    # password = 'order66'

    # if (username == 'pkelliott' or email == 'pk@elliott.com') and password == 'order66':
    #     print('Access Permitted.')
    # else:
    #   print('Access Denied.')

# sum of numbers 1-50
    # num = 50
    # sum = 0

    # while num > 0:
    #     sum += num
    #     num -= 1
    # print("the sum is ", sum)

# {name} is the winner!
    # name = 'Parker'

    # winner = f'{name} is the winner' if name == 'Parker' else '{name} is not the winner'

    # print (winner)

# Greeting Function

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

# fizzbuzz

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

# Dynamic Reducer (list of values being +, -, *, / by / to eachother)

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

    # print (dynamic_reducer([1, 2, 3], '+'))
    # print (dynamic_reducer([11, 12, 13], '-'))
    # print (dynamic_reducer([21, 22, 23], '*'))
    # print (dynamic_reducer([31, 32, 33], '/'))

# x_or (^=) difference between

    # def x_or(a, b):
    #     x = 0
    #     x ^= a
    #     x ^= b
    #     return x

    # print(x_or(12, 15))

# x_or single number

    # class Solution:

    #     numbers = [
    #         10,
    #         11,
    #         11,
    #         10,
    #         12
    #     ]

    #     def num_sorter(nums):
    #         x = 0
    #         for i in nums:
    #             x ^= i
    #         return x

    #     print(num_sorter(numbers))














