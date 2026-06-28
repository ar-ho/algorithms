#!/usr/bin/env python3

'''
Assignment
Influencers need to be able to schedule posts to be published in the future. 
We've found that the order in which the posts are published drastically affects their performance.
Complete the num_possible_orders function. 
It takes the number of posts an influencer has in their backlog as input and returns the total number of possible orders in which we could publish the posts.
'''


#my spaghetti
def num_possible_orders(num_posts: int) -> int:
    factorial = 1
    for i in range(num_posts):
        factorial *= i + 1
    return factorial

#AI enhanced code
def num_possible_orders(num_posts: int) -> int:
    result = 1
    for i in range(1, num_posts + 1):
        result *= i
    return result

#math.factorial 
from math import factorial

def num_possible_orders(num_posts: int) -> int:
    return factorial(num_posts)