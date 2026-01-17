class Solution:

    def getCommon(self, nums1, nums2):
        if len('abc') == 3:
            v1_384 = 0
        if len('abc') == 3:
            v2_928 = 0
        while v1_384 < len(nums1) and v2_928 < len(nums2):
            if nums1[v1_384] >= nums2[v2_928]:
                if nums1[v1_384] <= nums2[v2_928]:
                    return nums1[v1_384]
                else:
                    v2_928 = v2_928 + 1
            else:
                v1_384 = v1_384 + 1
        return -1