'''
Selection Sort

Another sorting algorithm we never covered in-depth is called "selection sort". It's similar to bubble sort in that it works by repeatedly swapping items in a list. However, it's slightly more efficient than bubble sort because it only makes one swap per iteration.

Selection sort pseudocode:

    For each index:
        Set smallest_idx to the current index (of the outer loop)
        For each index from i + 1 to the end of the list:
            If the number at the inner loop index is smaller than the number at smallest_idx, set smallest_idx to the inner loop index
        Swap the number at the outer loop index with the number at smallest_idx
    Return the sorted list

Assignment

Complete the selection_sort function.

It should sort the input list nums in ascending order using the selection sort algorithm. The function should then return the sorted list
'''

def selection_sort(nums):
    # Define a function called selection_sort that takes a list named nums.

    n = len(nums)
    # Store the number of elements in the list.

    for i in range(n):
        # Loop through each position in the list.
        # At each iteration, we will place the correct smallest value at index i.

        smallest_idx = i
        # Assume the current position contains the smallest element.

        # Find the smallest element in the unsorted part
        for j in range(i + 1, n):
            # Check every remaining element after index i.
            # example: n = [64, 25, 12, 22, 11], 
            # the number at index 0 is 64, at index 1 is 25, at index 2 is 12, at index 3 is 22, and at index 4 is 11
            # at the start j is at index 1 because we start at i + 1 and i is at index 0 because of the outer loop
            # smallest_idx is at index 0 because of smallest_idx = i and i is at index 0 because of the outer loop
            # if the number at nums[j] is smaller than the number at nums[smallest_idx] 
            # which is the case because nums[j] is 25 and nums[smallest_idx] is 64
            # then set smallest_idx to j, which is 1, smallest_idx is incremented from index 0 to index 1 and the loop continues
            # the next iteration j is now at index 2 and the value of nums[j] is 12, the value of nums[smallest_idx] is 25
            # which makes the if statement true again and smallest_idx is set to j, which is 2, the loop continues
            # we always compare the element at smallest_idx which is one index behind j (smallest_idx = j - 1) to the element at j, which is the current index of the inner loop
            # this process continues until the inner loop has checked all remaining elements in the list
            # in the end, smallest_idx will be at index 4 because the value of nums[smallest_idx] is 11, which is the smallest value in the list

            if nums[j] < nums[smallest_idx]:
                # If a smaller element is found...

                smallest_idx = j
                # ...remember its index.

        # Swap it into its correct position
        nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]
        # Swap the smallest element found with the element at index i.
        # the value of nums[i] i is at index 0 nums[0] would be set to the value of nums[smallest_idx] which is 11 
        # and the value of nums[smallest_idx] would be set to the value of nums[i] i is at index 0 nums[0] which is 64 
        # n aka nums would look like this after the swap: [11, 25, 12, 22, 64]
        # after this the outer loop increments i to 1 and the process repeats until the entire list is sorted
        # after the second iteration the list would look like this: [11, 12, 25, 22, 64] and so on until the list is sorted

    return nums
    # Return the now sorted list.