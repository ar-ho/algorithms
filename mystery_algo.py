#!/usr/bin/env python3

'''
    Start with input variables a and b
    Add a and b using the + operator, and assign the result to a new variable, sum
    Return the sum variable
'''
def summed(nums: list[int]) -> int:
    sum = 0
    for n in nums:
        sum += n
    return sum
