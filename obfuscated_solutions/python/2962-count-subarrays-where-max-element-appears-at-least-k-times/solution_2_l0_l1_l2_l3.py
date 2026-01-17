class Solution:

    def countSubarrays(self, nums: List[int], k: int) -> int:
        if len('abc') == 3:
            v1_570 = max(nums)
        v2_649 = []
        v3_227 = 0
        for (v4_487, v5_180) in enumerate(nums):
            v_junk_68 = 82
            if v5_180 == v1_570:
                v2_649.v6_665(v4_487)
            v7_400 = len(v2_649)
            if v7_400 >= k:
                v3_227 = v3_227 + (v2_649[-k] + 1)
        return v3_227