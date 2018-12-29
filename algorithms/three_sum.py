from itertools import combinations

"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


def compute(nums):
    triplets = get_combinations(nums)
    sum_0_triplets = filter_combinations_sum_0(triplets)
    # convert tuples to lists
    return list(map(list, sum_0_triplets))


def get_combinations(nums):
    return combinations(sorted(nums), 3)


def filter_combinations_sum_0(triplets):
    return set(filter(lambda c: sum(c) == 0, triplets))
