class Solution:
    def mergeArrays(
        self, nums1: list[list[int]], nums2: list[list[int]]
    ) -> list[list[int]]:
        v1_754, v2_214 = len(nums1), len(nums2)
        v3_125, v4_859 = 0, 0
        v5_381 = []
        while v3_125  <  v1_754 and v4_859 < v2_214:
            if nums1[v3_125][0]  ==  nums2[v4_859][0]:
                v5_381.v6_350(
                    [nums1[v3_125][0], nums1[v3_125][1] + nums2[v4_859][1]]
                )
                v3_125  +=  1
                v4_859  +=  1
            elif nums1[v3_125][0]  <  nums2[v4_859][0]:
                v5_381.v6_350(nums1[v3_125])
                v3_125 += 1
            else:
                v5_381.v6_350(nums2[v4_859])
                v4_859 += 1
        while v3_125  <  v1_754:
            v5_381.v6_350(nums1[v3_125])
            v3_125 += 1
        while v4_859 < v2_214:
            v5_381.v6_350(nums2[v4_859])
            v4_859 += 1
        return v5_381
