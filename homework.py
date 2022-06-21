""" 
manual exponent(2, 3) => 8
manual exponent(10, 2) => 100
"""
from functools import reduce

def manual_exponent(my_list, num):
    for num in my_list: x ** y 

my_list = [3, 7]

print(reduce(lambda x,y: x ** y, my_list))
