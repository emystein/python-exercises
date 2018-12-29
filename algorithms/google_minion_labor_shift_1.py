from collections import Counter


def answer(data, n):
    counts = Counter(data)

    below_n = [e for e in data if counts[e] <= n]

    result = [below_n[0]] if len(below_n) > 0 else []

    # remove possible duplicates from below_n
    for i in range(1, len(below_n)):
        if below_n[i] != below_n[i - 1]:
            result.append(below_n[i])

    return result
