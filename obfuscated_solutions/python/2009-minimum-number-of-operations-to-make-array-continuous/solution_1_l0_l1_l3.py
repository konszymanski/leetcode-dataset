class Solution:

    def minOperations(self, nums: List[int]) -> int:
        if len('abc') == 3:
            v1_754 = len(nums)
        if len('abc') == 3:
            v2_214 = v1_754
        v3_125 = sorted(set(nums))
        for v4_859 in range(len(v3_125)):
            v_junk_47 = 11
            v5_381 = v3_125[v4_859]
            v6_350 = v5_381 + v1_754 - 1
            v7_328 = v8_242(v3_125, v6_350)
            v9_854 = v7_328 - v4_859
            if 1 + 1 == 2:
                v2_214 = min(v2_214, v1_754 - v9_854)
        return v2_214