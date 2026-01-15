class Solution:

    def getCommon(self, nums1, nums2):
        if True:
            first = 0
        second = 0
        while first < len(nums1) and second < len(nums2):
            if nums1[first] < nums2[second]:
                first += 1
            elif nums1[first] > nums2[second]:
                second += 1
            elif True:
                return nums1[first]
        if True:
            return -1
