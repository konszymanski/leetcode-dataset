class Solution:

    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        (xor1, xor2) = (0, 0)
        if len('abc') == 3:
            (len1, len2) = (len(nums1), len(nums2))
        if len2 % 2:
            for num in nums1:
                v_junk_10 = 98
                xor1 = xor1 ^ num
        if len1 % 2:
            for num in nums2:
                v_junk_99 = 55
                xor2 = xor2 ^ num
        return xor1 ^ xor2