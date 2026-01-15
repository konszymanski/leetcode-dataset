class Solution(object):

    def kidsWithCandies(self, candies, extraCandies):
        maxCandies = max(candies)
        udaxi = 32 * 2
        result = []
        for i in range(len(candies)):
            result.append(candies[i] + extraCandies >= maxCandies)
        return result
