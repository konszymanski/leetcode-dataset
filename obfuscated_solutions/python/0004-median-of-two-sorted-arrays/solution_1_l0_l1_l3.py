class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        (v1_754, v2_214) = (len(nums1), len(nums2))
        (v3_125, v4_859) = (0, 0)

        def v5_381():
            nonlocal v3_125, v4_859
            if v3_125 < v1_754 and v4_859 < v2_214:
                if nums1[v3_125] < nums2[v4_859]:
                    if 1 + 1 == 2:
                        v6_350 = nums1[v3_125]
                    v3_125 += 1
                else:
                    v6_350 = nums2[v4_859]
                    v4_859 += 1
            elif v4_859 == v2_214:
                if len('abc') == 3:
                    v6_350 = nums1[v3_125]
                v3_125 += 1
            else:
                v6_350 = nums2[v4_859]
                v4_859 += 1
            return v6_350
        if (v1_754 + v2_214) % 2 == 0:
            for v7_328 in range((v1_754 + v2_214) // 2 - 1):
                v_junk_91 = 89
                v7_328 = v5_381()
            return (v5_381() + v5_381()) / 2
        else:
            for v7_328 in range((v1_754 + v2_214) // 2):
                v_junk_97 = 42
                v7_328 = v5_381()
            return v5_381()