#!/usr/bin/env python3

'''
for smaller code snippets
'''

#showcases the usage of math.log()
import math


def get_influencer_score(
    num_followers: int, average_engagement_percentage: float
) -> float:
    return average_engagement_percentage * math.log(num_followers, 2)

#exponential decay
def decayed_followers(
    initial_followers: int, fraction_lost_daily: float, days: int
) -> float:
    res = initial_followers * (1 - fraction_lost_daily) ** days
    return res

#logarithmic scale
import math

def log_scale(data: list[float], base: float) -> list[float]:
    new_list = []
    for d in data:
        new_list.append(math.log(d, base))
    return new_list

#average
def average_followers(nums: list[int]) -> float | None:
    result = 0
    if not nums:
        return None
    for n in nums:
        result += n
    return result / len(nums)

#highest engagement score
def find_max(nums: list[float]) -> float:
    highest = float("-inf")
    for num in nums:
        if num > highest:
            highest = num
    return highest

#order n squared, does name exist in the list of first and last names 
def does_name_exist(
    first_names: list[str], last_names: list[str], full_name: str
) -> bool:
    for f in first_names:
        for l in last_names:
            #combo = f"{f} {l}"
            if f"{f} {l}" == full_name:
                return True
    return False