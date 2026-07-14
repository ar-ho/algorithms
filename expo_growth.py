#!/usr/bin/env python3

'''
Assignment

While the influencers who use our platform are really great at taking selfies, most aren't super great at math. We need to write a tool that predicts an influencer's follower growth over time.

Complete the get_follower_prediction function. It takes a follower_count integer, an influencer_type string and a num_months integer, and returns an integer.

Calculate the number of followers an influencer will have after a given number of months according to the influencer type:

    "fitness": follower count quadruples each month
    "cosmetic": follower count triples each month
    other: follower count doubles each month

For example, if a "fitness" influencer starts with 10 followers, then after 1 month they would have 40 followers. After 2 months, they would have 160 followers, and so on.

This kind of sequence, where each term is found by multiplying the previous term by a constant, is called a geometric sequence or geometric progression.

Use the following version of the geometric progression formula, in which a1 is the initial number of followers, r is the multiplication constant, and n is the number of months:
'''

def get_follower_prediction(
    follower_count: int, influencer_type: str, num_months: int
) -> int:
    if influencer_type == "fitness":
        return follower_count * (4**num_months)
    if influencer_type == "cosmetic":
        return follower_count * (3**num_months)
    return follower_count * (2**num_months)

'''
Assignment

Complete the exponential_growth function. Given the initial followers count n, growth factor factor, and number of days days, return a list containing the exponential growth of followers for each day.

For example:

- Initial followers: 10
- Growth factor: 2
- Days: 4

Growth sequence: [10, 20, 40, 80, 160]

Each day's value is the previous day's value multiplied by factor.
'''

def exponential_growth(n: int, factor: int, days: int) -> list[int]:
    result = [n] 
    for d in range(days):
        n = n*factor
        result.append(n)
    return result