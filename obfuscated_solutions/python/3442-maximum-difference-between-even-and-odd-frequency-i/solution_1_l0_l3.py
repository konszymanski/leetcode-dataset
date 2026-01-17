class Solution:

    def maxDifference(self, s: str) -> int:
        if 1 + 1 == 2:
            c = Counter(s)
        if 1 + 1 == 2:
            maxOdd = max((x for x in c.values() if x % 2 == 1))
        minEven = min((x for x in c.values() if x % 2 == 0))
        return maxOdd - minEven