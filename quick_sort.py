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
    if low < high:

        # Partition the list around a pivot.
        # After partitioning, the pivot is in its final sorted position.
        p = partition(nums, low, high)

        # Recursively sort all elements to the left of the pivot.
        quick_sort(nums, low, p - 1)

        # Recursively sort all elements to the right of the pivot.
        quick_sort(nums, p + 1, high)


def partition(nums: list[int], low: int, high: int) -> int:
    # Choose the last element as the pivot.
    pivot = nums[high]

    # i keeps track of the position where the next smaller element
    # should be placed.
    # It starts one position before the beginning of the current section.
    i = low - 1

    # Examine every element except the pivot.
    for j in range(low, high):

        # If the current element is smaller than the pivot,
        # it belongs on the left side.
        if nums[j] < pivot:

            # Move the boundary between smaller and larger elements.
            i += 1

            # Swap the current element into the smaller-elements section.
            nums[i], nums[j] = nums[j], nums[i]

    # After all elements have been checked,
    # place the pivot immediately after the smaller elements.
    nums[i + 1], nums[high] = nums[high], nums[i + 1]

    # Return the pivot's final index.
    return i + 1