'''
Assignment:
Given two inputs:

    A list of n elements sorted from least to greatest
    A target value:

Do the following:

    Set low = 0 and high = n - 1.
    While low <= high:
        Set median (the position of the middle element) to (low + high) // 2, which is the greatest integer less than or equal to (low + high) / 2
        If list[median] == target, return True
        Else if list[median] < target, set low to median + 1
        Otherwise set high to median - 1
    Return False

At each iteration of loop, we halve the list. 
Which makes the algorithm O(log(n)). In other words, to add one more step to the runtime, we'd have to double the size of the input. 
Binary searches are fast.
'''

def binary_search(target: int, arr: list[int]) -> bool:
    low = 0
    high = len(arr) - 1
    while low <= high:
        median = (low + high) // 2
        if arr[median] == target:
            return True
        elif arr[median] < target:
            low = median + 1
        else:
            high = median - 1
    return False