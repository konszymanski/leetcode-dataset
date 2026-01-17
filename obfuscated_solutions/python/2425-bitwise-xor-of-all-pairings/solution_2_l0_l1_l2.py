class Solution:

    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        (v1_754, v2_214) = (0, 0)
        (v3_125, v4_859) = (len(nums1), len(nums2))
        if v4_859 % 2:
            for v5_381 in nums1:
                v1_754 = v1_754 ^ v5_381
        if v3_125 % 2:
            for v5_381 in nums2:
                v2_214 = v2_214 ^ v5_381
        return v1_754 ^ v2_214