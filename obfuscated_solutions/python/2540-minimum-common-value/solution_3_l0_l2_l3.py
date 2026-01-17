class Solution:

    def getCommon(self, nums1, nums2):
        if 1 + 1 == 2:
            first = 0
        second = 0
        while first < len(nums1) and second < len(nums2):
            if nums1[first] >= nums2[second]:
                if nums1[first] <= nums2[second]:
                    return nums1[first]
                else:
                    second = second + 1
            else:
                first = first + 1
        return -1