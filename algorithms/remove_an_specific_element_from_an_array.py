"""
www.codewars.com/kata/remove-an-specific-element-of-an-array
"""

from functools import reduce

def select_subarray(array):
    all_product = reduce(lambda x, y: x * y, array)
    sub_product = [all_product / element for element in array]
    all_sum = reduce(lambda x, y: x + y, array)
    sub_sum = [all_sum - element for element in array]
    quotients = [abs(sub_product / sub_sum) if sub_sum != 0 else abs(sub_product) for sub_product, sub_sum in zip(sub_product, sub_sum)]

    result = [[i, element] for i, (element, quotient) in enumerate(zip(array, quotients)) if quotient == min(quotients)]

    return result[0] if len(result) == 1 else result
