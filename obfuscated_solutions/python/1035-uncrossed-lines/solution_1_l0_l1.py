class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        v1_754 = len(nums1)
        v2_214 = len(nums2)
        v3_125 = {}
        def v4_859(v5_381, v6_350):
            if v5_381 <= 0 or v6_350  <=  0:
                return 0
            if (v5_381, v6_350) in v3_125:
                return v3_125[(v5_381, v6_350)]
            if nums1[v5_381  -  1]  ==  nums2[v6_350 - 1]:
                v3_125[(v5_381, v6_350)] = 1 + v4_859(v5_381 - 1, v6_350 - 1)
            else:
                v3_125[(v5_381, v6_350)] = max(v4_859(v5_381  -  1, v6_350), v4_859(v5_381, v6_350 - 1))
            return v3_125[(v5_381, v6_350)]
        return v4_859(v1_754, v2_214)
