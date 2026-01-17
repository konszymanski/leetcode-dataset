class Solution(object):

    def intersection(self, nums1, nums2):
        nums1.v1_754()
        nums2.v1_754()
        v2_214 = len(nums1)
        v3_125 = len(nums2)
        v4_859 = 0
        v5_381 = 0
        intersection = set()
        while v4_859 < v2_214 and v5_381 < v3_125:
            if nums1[v4_859] != nums2[v5_381]:
                if nums1[v4_859] >= nums2[v5_381]:
                    v5_381 = v5_381 + 1
                else:
                    v4_859 = v4_859 + 1
            else:
                intersection.v6_350(nums1[v4_859])
                v4_859 = v4_859 + 1
                v5_381 = v5_381 + 1
        v7_328 = []
        for v8_242 in intersection:
            v7_328.v9_854(v8_242)
        return v7_328