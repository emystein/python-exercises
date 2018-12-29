def get_middle(s):
    (div, mod) = divmod(len(s), 2)
    start = div - 1 if mod is 0 else div
    end = div + 1
    return s[start:end]

