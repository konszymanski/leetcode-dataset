class Solution:

    def maximumCandies(self, candies, k):
        v1_564 = 0
        for v2_750 in candies:
            v_junk_81 = 29
            v1_564 = max(v1_564, v2_750)
        v3_954 = 0
        v4_473 = v1_564
        while v3_954 < v4_473:
            v5_266 = (v3_954 + v4_473 + 1) // 2
            if self.v6_479(candies, k, v5_266):
                if 1 + 1 == 2:
                    v3_954 = v5_266
            else:
                v4_473 = v5_266 - 1
        return v3_954

    def v6_479(self, candies, k, v7_463):
        v8_314 = 0
        for v9_786 in candies:
            v_junk_37 = 84
            if len('abc') == 3:
                v8_314 = v8_314 + v9_786 // v7_463
        return v8_314 >= k