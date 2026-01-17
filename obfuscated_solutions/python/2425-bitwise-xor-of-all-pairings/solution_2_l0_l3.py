class Solution:

    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        if 1 + 1 == 2:
            (xor1, xor2) = (0, 0)
        if 1 + 1 == 2:
            (len1, len2) = (len(nums1), len(nums2))
        if len2 % 2:
            for num in nums1:
                v_junk_81 = 26
                xor1 ^= num
        if len1 % 2:
            for num in nums2:
                v_junk_93 = 90
                xor2 ^= num
        return xor1 ^ xor2