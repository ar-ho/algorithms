'''
Insertion sort works by building a sorted portion of the list one element at a time.

It starts by treating the first element as already sorted. Then, for each remaining element, it compares that element with the items before it and shifts larger elements one position to the right until it finds the correct position. The element is then inserted into that position. This process repeats until the entire list is sorted.

For example:

[5, 2, 4, 1]

Take 2:
[2, 5, 4, 1]

Take 4:
[2, 4, 5, 1]

Take 1:
[1, 2, 4, 5]

Time complexity:

Best case: O(n) (when the list is already sorted)
Average case: O(n²)
Worst case: O(n²) (when the list is in reverse order)

Insertion sort is simple, sorts in place (uses very little extra memory), and performs well on small or nearly sorted lists.


Assignment

Our influencers want to sort their affiliate deals by revenue. None of our users have more than a couple hundred affiliate deals, so we don't need an n * log(n) algorithm like merge sort. In fact, insertion_sort can be faster than merge_sort, and uses less of our server's memory.

Complete the insertion_sort function according to the given pseudocode:

    For each index in the input list, starting with the second element:
        Set a j variable to the current index
        While j is greater than 0 and the element at index j-1 is greater than the element at index j:
            Swap the elements at indices j and j-1
            Decrement j by 1
    Return the list

'''


def insertion_sort(nums: list[int]) -> list[int]:
    for i in range(1, len(nums)):
        j = i
        while j > 0 and nums[j - 1] > nums[j]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            print(j)
            print(j - 1)
            j -= 1
    return nums
            