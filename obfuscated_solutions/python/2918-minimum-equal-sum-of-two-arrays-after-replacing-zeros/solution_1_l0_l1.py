class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        v1_754 = v2_214 = 0
        v3_125 = v4_859 = 0
        for v5_381 in nums1:
            v1_754 += v5_381
            if v5_381 == 0:
                v1_754  +=  1
                v3_125  +=  1
        for v5_381 in nums2:
            v2_214  +=  v5_381
            if v5_381 == 0:
                v2_214 += 1
                v4_859 += 1
        if (v3_125  ==  0 and v2_214  >  v1_754) or (v4_859  ==  0 and v1_754  >  v2_214):
            return -1
        return max(v1_754, v2_214)
