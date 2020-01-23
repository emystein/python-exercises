"""
Kata: https://www.codewars.com/kata/5b0d67c1cb35dfa10b0022c7

I assume most of you are familiar with the ancient legend of the rice (but I see wikipedia suggests wheat, for some reason) problem, but a quick recap for you: a young man asks as a compensation only 1 grain of rice for the first square, 2 grains for the second, 4 for the third, 8 for the fourth and so on, always doubling the previous.

Your task is pretty straightforward (but not necessarily easy): given an amount of grains, you need to return up to which square of the chessboard one should count in order to get at least as many.

As usual, a few examples might be way better than thousands of words from me:

squaresNeeded(0) === 0
squaresNeeded(1) === 1
squaresNeeded(2) === 2
squaresNeeded(3) === 2
squaresNeeded(4) === 3
"""
import math


def squares_needed(grains):
    if grains == 0:
        return 0
    else:
        return math.floor(math.log(grains, 2)) + 1

