#!/usr/bin/env python3

'''

Assignment

In the social media industry, there is a concept called "spread": how much a post spreads due to "reshares" after all of the original author's followers see it. As it turns out, social media posts spread at an exponential rate! We've found that the estimated spread of a post can be calculated with this formula:

estimated_spread = average_audience_followers * ( num_followers ** 1.2 )

In the formula above, average_audience_followers is the average of the numbers in the audiences_followers list. This list contains the individual follower counts of the author's followers. For example, if audiences_followers = [2, 3, 2, 19], then:

    the author has 4 total followers
    each follower has their own 2, 3, 2, and 19 followers, respectively.

Complete the get_estimated_spread function by implementing the formula above. The only input is audiences_followers, which is a list of the follower counts of all the followers the author has. Return the estimated spread. If the audiences_followers list is empty, return 0.
'''

#my spaghetti code
def get_estimated_spread(audiences_followers: list[int]) -> float:
    num_followers = len(audiences_followers)
    estimated_spread = 0
    average_audiences_followers = 0
    if not audiences_followers:
        return 0
    for a in audiences_followers:
        average_audiences_followers += a 
    average_audiences_followers = average_audiences_followers / num_followers
    estimated_spread = average_audiences_followers * ( num_followers ** 1.2 )
    return estimated_spread


#a more optimized pythonic version
def get_estimated_spread(audiences_followers: list[int]) -> float:
    if not audiences_followers:
        return 0.0

    audience_count = len(audiences_followers)
    average_followers = sum(audiences_followers) / audience_count

    return average_followers * (audience_count ** 1.2)