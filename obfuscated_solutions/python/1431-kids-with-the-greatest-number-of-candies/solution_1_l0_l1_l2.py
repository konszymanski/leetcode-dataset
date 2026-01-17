class Solution(object):

    def kidsWithCandies(self, candies, extraCandies):
        v1_754 = max(candies)
        v2_214 = []
        for v3_125 in range(len(candies)):
            v2_214.v4_859(candies[v3_125] + extraCandies >= v1_754)
        return v2_214