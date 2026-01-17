class Solution:
    def intersection(self, nums1, nums2):
        v1_754 = set(nums1)
        v2_214 = set(nums2)
        return list(v2_214 & v1_754)
