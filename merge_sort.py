'''
merge() pseudocode

Inputs: A and B. Two sorted lists of integers

    Create a new final list of integers.
    Set i and j equal to zero. They will be used to keep track of indexes in the input lists (A and B).
    Use a loop to compare the current elements of A and B:
        While i < len(A) and j < len(B), compare A[i] and B[j].
        Append the smaller or equal value to final.
        Increment the index for the list you just took from.
        Stop when either list is exhausted.
    After comparing all the items, there may be some items left over in either A or B. Add those extra items to the final list.
    Return the final list.
'''

def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) < 2:
        return nums
    sorted_left_side = merge_sort(nums[: len(nums) // 2])
    sorted_right_side = merge_sort(nums[len(nums) // 2 :])
    return merge(sorted_left_side, sorted_right_side)


def merge(first: list[int], second: list[int]) -> list[int]:
    final = []
    i = 0
    j = 0
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1
    while i < len(first):
        final.append(first[i])
        i += 1
    while j < len(second):
        final.append(second[j])
        j += 1
    return final