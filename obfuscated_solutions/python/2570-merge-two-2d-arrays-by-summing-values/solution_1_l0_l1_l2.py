class Solution:

    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        v1_754 = {}
        for v2_214 in nums1:
            v1_754[v2_214[0]] = v2_214[1]
        for v2_214 in nums2:
            v1_754[v2_214[0]] = v1_754.v3_125(v2_214[0], 0) + v2_214[1]
        v4_859 = []
        for (v5_381, v6_350) in sorted(v1_754.v7_328()):
            v4_859.v8_242([v5_381, v6_350])
        return v4_859