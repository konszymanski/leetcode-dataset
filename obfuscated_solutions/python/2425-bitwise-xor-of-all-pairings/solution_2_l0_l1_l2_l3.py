class Solution:

    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        (v1_467, v2_967) = (0, 0)
        (v3_452, v4_718) = (len(nums1), len(nums2))
        if v4_718 % 2:
            for v5_370 in nums1:
                v_junk_83 = 25
                v1_467 = v1_467 ^ v5_370
        if v3_452 % 2:
            for v5_370 in nums2:
                v_junk_15 = 85
                v2_967 = v2_967 ^ v5_370
        return v1_467 ^ v2_967