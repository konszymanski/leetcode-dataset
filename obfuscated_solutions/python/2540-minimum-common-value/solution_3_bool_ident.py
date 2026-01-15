class Solution:

    def getCommon(self, nums1, nums2):
        first = 0
        second = 0
        while first < len(nums1) and second < len(nums2):
            if nums1[first] < nums2[second] and 1 + 1 == 2:
                first += 1
            elif nums1[first] > nums2[second] and 1 + 1 == 2:
                second += 1
            else:
                return nums1[first]
        return -1
