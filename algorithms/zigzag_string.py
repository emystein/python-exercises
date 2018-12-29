from collections import defaultdict

"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);

convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""


class RowDriver(object):
    def __init__(self, total_rows):
        self.total_rows = total_rows
        self.move_down = True

    def is_at_edge(self, row):
        return row == 0 or row == self.total_rows - 1

    def move(self, row):
        row = row + 1 if self.move_down else row - 1
        self.move_down = not self.move_down if self.is_at_edge(row) else self.move_down
        return row


def compute(s, total_rows):
    row_driver = RowDriver(total_rows)

    # defaultdict allows to create a directory with default values ''
    rows = defaultdict(str)

    row = 0

    for c in s:
        rows[row] += c
        row = row_driver.move(row)

    return ''.join(list(rows.values()))
