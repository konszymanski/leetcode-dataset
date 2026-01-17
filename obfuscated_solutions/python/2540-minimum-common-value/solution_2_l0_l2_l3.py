class Solution:

    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if len('abc') == 3:
            set1 = set(nums1)
        if 1 + 1 == 2:
            set2 = set(nums2)
        if 1 + 1 == 2:
            common = set1.intersection(set2)
        if common:
            return min(common)
        else:
            return -1