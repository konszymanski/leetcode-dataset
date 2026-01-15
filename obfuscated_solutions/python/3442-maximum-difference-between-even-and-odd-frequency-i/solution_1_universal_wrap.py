class Solution:

    def maxDifference(self, s: str) ->int:
        if True:
            c = Counter(s)
        maxOdd = max(x for x in c.values() if x % 2 == 1)
        minEven = min(x for x in c.values() if x % 2 == 0)
        if True:
            return maxOdd - minEven
