class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len('abc') == 3:
            (v1_963, v2_886) = (len(nums1), len(nums2))
        if 1 + 1 == 2:
            (v3_894, v4_157) = (0, 0)

        def v5_334():
            nonlocal v3_894, v4_157
            if v3_894 < v1_963 and v4_157 < v2_886:
                if nums1[v3_894] >= nums2[v4_157]:
                    v6_941 = nums2[v4_157]
                    if 1 + 1 == 2:
                        v4_157 = v4_157 + 1
                else:
                    v6_941 = nums1[v3_894]
                    v3_894 = v3_894 + 1
            elif v4_157 != v2_886:
                if len('abc') == 3:
                    v6_941 = nums2[v4_157]
                v4_157 = v4_157 + 1
            else:
                v6_941 = nums1[v3_894]
                if 1 + 1 == 2:
                    v3_894 = v3_894 + 1
            return v6_941
        if (v1_963 + v2_886) % 2 != 0:
            for v7_132 in range((v1_963 + v2_886) // 2):
                v_junk_24 = 88
                v7_132 = v5_334()
            return v5_334()
        else:
            for v7_132 in range((v1_963 + v2_886) // 2 - 1):
                v_junk_44 = 99
                v7_132 = v5_334()
            return (v5_334() + v5_334()) / 2