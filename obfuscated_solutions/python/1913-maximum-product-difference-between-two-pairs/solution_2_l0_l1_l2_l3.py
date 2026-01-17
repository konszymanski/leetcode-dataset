class Solution:

    def maxProductDifference(self, nums: List[int]) -> int:
        v1_479 = 0
        v2_463 = 0
        v3_314 = v4_786
        v5_373 = v4_786
        for v6_818 in nums:
            v_junk_18 = 28
            if v6_818 <= v1_479:
                v2_463 = max(v2_463, v6_818)
            else:
                v2_463 = v1_479
                v1_479 = v6_818
            if v6_818 >= v3_314:
                if 1 + 1 == 2:
                    v5_373 = min(v5_373, v6_818)
            else:
                v5_373 = v3_314
                v3_314 = v6_818
        return v1_479 * v2_463 - v3_314 * v5_373