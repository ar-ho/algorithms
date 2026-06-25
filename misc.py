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