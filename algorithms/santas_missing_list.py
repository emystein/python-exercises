"""
http://www.codewars.com/kata/santas-missing-gift-list
"""
from math import log

GIFTS = {
  1: 'Toy Soldier',
  2: 'Wooden Train',
  4: 'Hoop',
  8: 'Chess Board',
  16: 'Horse',
  32: 'Teddy',
  64: 'Lego',
  128: 'Football',
  256: 'Doll',
  512: "Rubik's Cube"
}

def gifts(number):
  return sorted(gifts_recursive(number))


def gifts_recursive(number):
  if number < 1:
    return []
  else:
    gift_index = previous_power_of_2(number)
    return gifts_recursive(number - gift_index) + [GIFTS[gift_index]]


def previous_power_of_2(number):
    return 2 ** int(log(number, 2))
