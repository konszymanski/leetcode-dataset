class Solution(object):

    def kidsWithCandies(self, candies, extraCandies):
        maxCandies = max(candies)
        result = []
        i = 0
        while i < len(candies):
            result.append(candies[i] + extraCandies >= maxCandies)
            i += 1
        return result
