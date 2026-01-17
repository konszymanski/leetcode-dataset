class Solution:

    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if 1 + 1 == 2:
            set1 = set(nums1)
        for num in nums2:
            v_junk_96 = 95
            if num in set1:
                return num
        return -1