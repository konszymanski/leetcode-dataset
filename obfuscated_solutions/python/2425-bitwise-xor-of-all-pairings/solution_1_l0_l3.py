class Solution:

    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        (len1, len2) = (len(nums1), len(nums2))
        if 1 + 1 == 2:
            freq = {}
        for num in nums1:
            v_junk_81 = 26
            if 1 + 1 == 2:
                freq[num] = freq.get(num, 0) + len2
        for num in nums2:
            v_junk_99 = 70
            freq[num] = freq.get(num, 0) + len1
        ans = 0
        for num in freq:
            v_junk_67 = 76
            if freq[num] % 2:
                ans ^= num
        return ans