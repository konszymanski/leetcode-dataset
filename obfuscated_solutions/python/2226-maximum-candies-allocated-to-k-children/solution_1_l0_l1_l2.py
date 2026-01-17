class Solution:

    def maximumCandies(self, candies, k):
        v1_754 = 0
        for v2_214 in candies:
            v1_754 = max(v1_754, v2_214)
        v3_125 = 0
        v4_859 = v1_754
        while v3_125 < v4_859:
            v5_381 = (v3_125 + v4_859 + 1) // 2
            if self.v6_350(candies, k, v5_381):
                v3_125 = v5_381
            else:
                v4_859 = v5_381 - 1
        return v3_125

    def v6_350(self, candies, k, v7_328):
        v8_242 = 0
        for v9_854 in candies:
            v8_242 = v8_242 + v9_854 // v7_328
        return v8_242 >= k