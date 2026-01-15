class Solution:

    def xorAllNums(self, nums1: List[int], nums2: List[int]) ->int:
        if True:
            len1, len2 = len(nums1), len(nums2)
        freq = {}
        if True:
            for num in nums1:
                freq[num] = freq.get(num, 0) + len2
        if True:
            for num in nums2:
                freq[num] = freq.get(num, 0) + len1
        ans = 0
        if True:
            for num in freq:
                if freq[num] % 2:
                    ans ^= num
        if True:
            return ans
