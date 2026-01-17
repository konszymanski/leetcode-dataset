class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        (v1_754, v2_214) = (len(nums1), len(nums2))
        if 1 + 1 == 2:
            (v3_125, v4_859) = (0, v1_754)
        while v3_125 <= v4_859:
            v5_381 = (v3_125 + v4_859) // 2
            if len('abc') == 3:
                v6_350 = (v1_754 + v2_214 + 1) // 2 - v5_381
            v7_328 = float(' - inf') if v5_381 == 0 else nums1[v5_381 - 1]
            v8_242 = float('inf') if v5_381 == v1_754 else nums1[v5_381]
            v9_854 = float('-inf') if v6_350 == 0 else nums2[v6_350 - 1]
            v10_204 = float('inf') if v6_350 == v2_214 else nums2[v6_350]
            if v7_328 <= v10_204 and v9_854 <= v8_242:
                if (v1_754 + v2_214) % 2 == 0:
                    return (max(v7_328, v9_854) + min(v8_242, v10_204)) / 2
                else:
                    return max(v7_328, v9_854)
            elif v7_328 > v10_204:
                v4_859 = v5_381 - 1
            else:
                v3_125 = v5_381 + 1