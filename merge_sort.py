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
    # Base case: if the list has 0 or 1 element, it is already sorted.
    # The recursion stops here to prevent infinite recursive calls.
    if len(nums) < 2:
        return nums

    # Recursively sort the left half of the list.
    # nums[:len(nums)//2] creates a new list containing the first half.
    sorted_left_side = merge_sort(nums[: len(nums) // 2])

    # Recursively sort the right half of the list.
    # nums[len(nums)//2:] creates a new list containing the second half.
    sorted_right_side = merge_sort(nums[len(nums) // 2 :])

    # Merge the two sorted halves into one sorted list.
    return merge(sorted_left_side, sorted_right_side)


def merge(first: list[int], second: list[int]) -> list[int]:
    # Create an empty list that will contain the merged, sorted result.
    final = []

    # i points to the current element in the first list.
    i = 0

    # j points to the current element in the second list.
    j = 0

    # Continue as long as both lists still have elements remaining.
    while i < len(first) and j < len(second):

        # Compare the current elements of both lists.
        # Because both lists are already sorted, the smaller value
        # must be the next value in the final sorted list.
        if first[i] <= second[j]:
            final.append(first[i])  # Add the smaller element.
            i += 1                  # Move to the next element in the first list.
        else:
            final.append(second[j]) # Add the smaller element from the second list.
            j += 1                  # Move to the next element in the second list.

    # If there are elements left in the first list,
    # append all of them to the result.
    # They are already sorted and larger than everything already added.
    while i < len(first):
        final.append(first[i])
        i += 1

    # Do the same for any remaining elements in the second list.
    while j < len(second):
        final.append(second[j])
        j += 1

    # Return the completely merged and sorted list.
    return final