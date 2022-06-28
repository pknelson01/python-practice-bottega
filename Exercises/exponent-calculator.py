""" 
manual exponent(2, 3) => 8
manual exponent(10, 2) => 100
"""
from functools import reduce

print('Input number')

a = int(input())

print('Input exponent value')

b = int(input())

my_list = [a, b]

def manual_exponent(my_list, num):
    for num in my_list: x ** y

print(reduce(lambda x,y: x ** y, my_list))
