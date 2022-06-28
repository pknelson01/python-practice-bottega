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


# class SeperateSolution:

def x_or(a, b):
    x = 0
    x ^= a
    x ^= b
    return x

print(x_or(12, 15))