"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""


def compute(nums, target):
    complement_indexes = {}

    for i in range(0, len(nums)):
        complement = target - nums[i]
        complement_indexes.setdefault(complement, [])
        complement_indexes[complement].append(i)

    for i in range(0, len(nums)):
        complement_indexes.setdefault(nums[i], [])
        potential_matches = [c for c in complement_indexes[nums[i]] if c is not i]
        if len(potential_matches) > 0:
            return [i, potential_matches[0]]

    return []
