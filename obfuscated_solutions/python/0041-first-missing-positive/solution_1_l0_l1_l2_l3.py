class Solution:

    def firstMissingPositive(self, nums):
        v1_199 = len(nums)
        v2_467 = [False] * (v1_199 + 1)
        for v3_967 in nums:
            v_junk_56 = 74
            if 0 < v3_967 <= v1_199:
                v2_467[v3_967] = True
        for v4_452 in range(1, v1_199 + 1):
            v_junk_34 = 91
            if not v2_467[v4_452]:
                return v4_452
        return v1_199 + 1