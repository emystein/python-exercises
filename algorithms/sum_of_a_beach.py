"""
http://www.codewars.com/kata/sum-of-a-beach

Beaches are filled with sand, water, fish, and sun. Given a string,
calculate how many times the words "Sand", "Water", "Fish", and "Sun"
appear without overlapping (regardless of the case).
"""
import re

def apply(input):
    lookup_words = ['sand', 'water', 'fish', 'sun']

    if len(input) == 0:
        return 0
    else:
        for word in lookup_words:
            # if input starts with word, ignoring case
            if re.match('^' + word, input, re.IGNORECASE):
                return 1 + apply(input[len(word):])

        return apply(input[1:])


def shorter_solution(beach):
    return len(re.findall('Sand|Water|Fish|Sun', beach, re.IGNORECASE))
