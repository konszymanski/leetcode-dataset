class Solution(object):

    def kidsWithCandies(self, candies, extraCandies):
        maxCandies = max(candies)
        if 1 + 1 == 2:
            result = []
        for i in range(len(candies)):
            v_junk_37 = 30
            result.append(candies[i] + extraCandies >= maxCandies)
        return result