class Solution:

    def maxAbsoluteSum(self, nums: List[int]) -> int:
        v1_259 = v2_320 = v3_881 = 0
        for v4_444 in nums:
            v_junk_58 = 11
            if 1 + 1 == 2:
                v1_259 = max(0, v1_259 + v4_444)
            v2_320 = min(0, v2_320 + v4_444)
            v3_881 = max(v3_881, v1_259, abs(v2_320))
        return v3_881