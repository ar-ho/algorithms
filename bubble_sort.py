'''
Bubble sort repeatedly steps through a slice and compares adjacent elements, swapping them if they are out of order. It continues to loop over the slice until the whole list is completely sorted. Here's the pseudocode:

    Set swapping to True
    Set end to the length of the input list
    While swapping is True:
        Set swapping to False
        For i from the 2nd element to end:
            If the (i-1)th element of the input list is greater than the ith element:
                Swap the (i-1)th element and the ith element
                Set swapping to True
        Decrement end by one
    Return the sorted list

Bubble sort is a simple sorting algorithm that repeatedly compares adjacent elements in a list 
and swaps them if they are in the wrong order. 
After each pass through the list, the largest unsorted element "bubbles" to its correct position at the end. 
This process continues until no more swaps are needed, meaning the list is sorted.

The for loop is the part where the array is sorted. 
Each iteration of the for loops results in the higest number of the range(1, end) bubbling to the end of the list.
That's why end -= 1 is needed to reduce the range of the for loop, since the last element is already sorted and is the highest number in the list.
The next iteration then again bubbles the next highest number to the end of the list, and so on, until the entire list is sorted.
The exit condition of the while loop is when end shrinks down to 1.
That means nums[i - 1] results to 0 and nums[i] results to 1
and the if condition nums[i - 1] > nums[i] results to False since nums[0] is not greater than nums[1] and swapping remains False,
swapping = True is not executed, exiting the while loop and returning the sorted list. 

'''

def bubble_sort(nums: list[int]) -> list[int]:
    swapping = True
    end = len(nums)
    while swapping:
        swapping = False
        for i in range(1, end):
            if nums[i - 1] > nums[i]:
                temp = nums[i - 1]
                nums[i - 1] = nums[i]
                nums[i] = temp
                swapping = True
        end -= 1
    return nums