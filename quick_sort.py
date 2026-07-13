'''
Assignment

We now have two sorting algorithms on our LockedIn backend! It is a bit annoying to maintain both in the codebase. Quicksort is fast on large datasets just like merge sort, but is also lighter on memory usage. Let's use quick sort for both follower count and influencer revenue sorting!

Complete the quick_sort and partition functions according to the given algorithms.

The process is started with quick_sort(A, 0, len(A)-1).

    Complete quick_sort(nums, low, high):
        If low is less than high:
            Partition the input list using the partition function and store the returned "middle" index
            Recursively call quick_sort on the elements left of the pivot (low to middle - 1)
            Recursively call quick_sort on the elements right of the pivot (middle + 1 to high)
    partition(nums, low, high):
        Set pivot to the element at index high
        Set i to the index before low
        For each index (j) in range(low, high):
            If the element at index j is less than the pivot:
                Increment i by 1
                Swap the element at index i with the element at index j
        Swap the element at index i + 1 with the element at index high (the pivot's position)
        Return i + 1 (the pivot's new index)
'''

def quick_sort(nums: list[int], low: int, high: int) -> None:
    # Check if the current section of the list contains at least two elements.
    # If low >= high, the section is already sorted (0 or 1 element).
    # Low is the starting index of the section, and high is the ending index.
    # Starting values usually are: low = 0 and high = len(nums) - 1 (length of nums minus 1, the index of the last element).

    if low < high:

        # Partition the list around a pivot.
        # After partitioning, the pivot is in its final sorted position.
        p = partition(nums, low, high)

        # Recursively sort all elements to the left of the pivot.
        # Using the list from the partition run [3,5,2,7,8]
        # This means low is 0 and p is 3 - 1, i.e. the [3,5,2] section of the list will be sorted in the next recursive call.
        quick_sort(nums, low, p - 1)

        # Recursively sort all elements to the right of the pivot.
        # Using the list from the partition run [3,5,2,7,8]
        # This means p is 3 + 1 and high is 4, i.e. the [8] section of the list will be sorted in the next recursive call.
        quick_sort(nums, p + 1, high)

        # This happens over and over again until the condition low < high is no longer true, which means the list is sorted.

def partition(nums: list[int], low: int, high: int) -> int:
    # Choose the last element as the pivot.
    pivot = nums[high]

    # i keeps track of the position where the next smaller element should be placed.
    # It starts one position before the beginning of the current section.
    # i is never accessed directly; it is only used to determine where to place the next smaller element.
    # This won't lead to an IndexError when low = 0 and therefore i = -1 
    # because the first time we increment i, it will be equal to low i.e. 0, which is a valid index.
    i = low - 1

    # Examine every element except the pivot.
    for j in range(low, high):

        # If the current element is smaller than the pivot,
        # it belongs on the left side.
        # example: nums = [8, 3, 5, 2, 7]
        # nums[j] is nums [0] because j is at the starting value of 0 and the value is 8
        # the value of pivot is 7 because it is the last element in the list
        # that means the condition is false and we do not enter the if statement
        # the loop iteration continues and j is now 1 and the value of nums[j] is 3, i is still -1 and pivot is still 7
        # the condition is true and we enter the if statement, increment i to 0 and swap nums[0] with nums[1] so the list becomes [3, 8, 5, 2, 7]
        # and so on until the loop is finished the list after the last iteration is [3, 2, 5, 8, 7] and i is 2
        if nums[j] < pivot:

            # Move the boundary between smaller and larger elements.
            i += 1

            # Swap the current element into the smaller-elements section.
            nums[i], nums[j] = nums[j], nums[i]

    # After all elements have been checked,
    # place the pivot immediately after the smaller elements.
    # i always one index behind the pivot, that's why we swap nums[i + 1] with nums[high] (the pivot).
    # this swaps the pivot at nums[i + 1] with the element at nums[high] (the pivot's original position).
    # the list looks like this afterwards [3,5,2,7,8]
    nums[i + 1], nums[high] = nums[high], nums[i + 1]

    # Return the pivot's final index.
    # Which the index of 3 (the value is 7 but does not get returned) 
    return i + 1