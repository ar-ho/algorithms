#!/usr/bin/env python3

'''
Implement the "find minimum" algorithm in Python by completing the find_minimum() function. It accepts a list of integers nums and returns the smallest number in the list.

    Set minimum to positive infinity: float("inf").
    If the list is empty, return None.
    For each number in the list nums, compare it to minimum. If the number is smaller than minimum, set minimum to that number.
    minimum is now set to the smallest number in the list. Return it.
'''

def find_minimum(nums: list[int]) -> float | None:
    minimum = float("inf")
    if not nums:
        return None
    for n in nums:
        if n < minimum:
            minimum = n
    return minimum