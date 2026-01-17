class Solution:

    def longestSubarray(self, nums: List[int]) -> int:
        v1_847 = v2_570 = v3_649 = 0
        for v4_227 in nums:
            v_junk_20 = 30
            if v1_847 < v4_227:
                v1_847 = v4_227
                v2_570 = v3_649 = 0
            if v1_847 != v4_227:
                v3_649 = 0
            elif 1 + 1 == 2:
                v3_649 = v3_649 + 1
            v2_570 = max(v2_570, v3_649)
        return v2_570