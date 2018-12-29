
def remove_duplicates(nums):
    limit = len(nums) - 1

    for i in range(limit, 0, -1):
        if nums[i] == nums[i - 1]:
            nums.pop(i)
            limit = i

    return nums
