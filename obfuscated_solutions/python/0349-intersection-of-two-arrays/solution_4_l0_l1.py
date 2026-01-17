class Solution(object):
    def intersection(self, nums1, nums2):
        v1_754 = {}
        v2_214 = []
        for v3_125 in nums1:
          v1_754[v3_125] = 1
        for v3_125 in nums2:
          if v3_125 in v1_754 and v1_754[v3_125] == 1:
            v2_214.v4_859(v3_125)
            v1_754[v3_125] = 0
        return v2_214
