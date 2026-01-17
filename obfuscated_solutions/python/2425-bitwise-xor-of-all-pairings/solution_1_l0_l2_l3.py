class Solution:

    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        if 1 + 1 == 2:
            (len1, len2) = (len(nums1), len(nums2))
        freq = {}
        for num in nums1:
            v_junk_53 = 36
            if len('abc') == 3:
                freq[num] = freq.get(num, 0) + len2
        for num in nums2:
            v_junk_23 = 12
            if len('abc') == 3:
                freq[num] = freq.get(num, 0) + len1
        ans = 0
        for num in freq:
            v_junk_54 = 78
            if freq[num] % 2:
                ans = ans ^ num
        return ans