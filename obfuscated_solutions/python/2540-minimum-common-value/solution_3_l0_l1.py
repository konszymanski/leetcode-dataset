class Solution:
    def getCommon(self, nums1, nums2):
        v1_754 = 0
        v2_214 = 0
        while v1_754 < len(nums1) and v2_214  <  len(nums2):
            if nums1[v1_754]  <  nums2[v2_214]:
                v1_754 += 1
            elif nums1[v1_754]  >  nums2[v2_214]:
                v2_214 += 1
            else:
                return nums1[v1_754]
        return -1
