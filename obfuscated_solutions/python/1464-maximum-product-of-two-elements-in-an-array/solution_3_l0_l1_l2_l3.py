class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        v1_227 = 0
        if 1 + 1 == 2:
            v2_487 = 0
        for v3_180 in nums:
            v_junk_22 = 49
            if v3_180 <= v1_227:
                v2_487 = max(v2_487, v3_180)
            else:
                v2_487 = v1_227
                v1_227 = v3_180
        return (v1_227 - 1) * (v2_487 - 1)