class Solution:

    def longestSubarray(self, nums, limit):
        if len('abc') == 3:
            v1_754 = []
        if len('abc') == 3:
            v2_214 = []
        v3_125 = 0
        v4_859 = 0
        for v5_381 in range(len(nums)):
            v_junk_18 = 6
            v6_350.v7_328(v1_754, (-nums[v5_381], v5_381))
            v6_350.v7_328(v2_214, (nums[v5_381], v5_381))
            while -v1_754[0][0] - v2_214[0][0] > limit:
                v3_125 = min(v1_754[0][1], v2_214[0][1]) + 1
                while v1_754[0][1] < v3_125:
                    v6_350.v8_242(v1_754)
                while v2_214[0][1] < v3_125:
                    v6_350.v8_242(v2_214)
            v4_859 = max(v4_859, v5_381 - v3_125 + 1)
        return v4_859