from typing import List


def radixSortMSD(strings: List[str], d: int) -> List[str]:
    if len(strings) <= 1:
        return strings

    buckets = {}
    for s in strings:
        if d < len(s):
            char = s[d]
        else:
            char = "*"

        if char not in buckets:
            buckets[char] = []

        buckets[char].append(s)

    sortedStrings = []
    for char in sorted(buckets.keys()):
        sortedStrings += radixSortMSD(buckets[char], d+1)

    return sortedStrings


strings = ["ba", "abc", "ab", "b"]
print(radixSortMSD(strings, 0))