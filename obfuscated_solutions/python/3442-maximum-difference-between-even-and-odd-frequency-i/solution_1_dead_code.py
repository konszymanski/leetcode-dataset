class Solution:

    def maxDifference(self, s: str) ->int:
        c = Counter(s)
        udaxi = 32 * 2
        maxOdd = max(x for x in c.values() if x % 2 == 1)
        minEven = min(x for x in c.values() if x % 2 == 0)
        return maxOdd - minEven
