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

# Idea:
#   take 2 negatives and find positive complement
#   take 2 positives and find negative complement
from itertools import combinations


def compute(nums):
    result = []

    negative_numbers = sorted(list(filter(lambda n: n < 0, nums)))
    positive_numbers = sorted(list(filter(lambda n: n >= 0, nums)))

    add_triplets(negative_numbers, positive_numbers, result)
    add_triplets(positive_numbers, negative_numbers, result)

    return sorted(result)


def add_triplets(filtered_numbers, disjoint_numbers, result):
    if filtered_numbers[:3] == [0, 0, 0]:
        result.append([0, 0, 0])

    number_tuples = combinations(filtered_numbers, 2)

    for t in number_tuples:
        complement = sum(t) * -1
        if complement in disjoint_numbers:
            triplet = sorted([t[0], t[1], complement])
            if triplet not in result:
                result.append(triplet)
