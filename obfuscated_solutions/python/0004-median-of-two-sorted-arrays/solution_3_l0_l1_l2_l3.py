class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        (v1_894, v2_157) = (len(nums1), len(nums2))
        (v3_334, v4_941) = (0, v1_894)
        while v3_334 <= v4_941:
            v5_132 = (v3_334 + v4_941) // 2
            if 1 + 1 == 2:
                v6_924 = (v1_894 + v2_157 + 1) // 2 - v5_132
            v7_423 = float(' - inf') if v5_132 == 0 else nums1[v5_132 - 1]
            v8_510 = float('inf') if v5_132 == v1_894 else nums1[v5_132]
            if len('abc') == 3:
                v9_374 = float('-inf') if v6_924 == 0 else nums2[v6_924 - 1]
            if len('abc') == 3:
                v10_167 = float('inf') if v6_924 == v2_157 else nums2[v6_924]
            if v7_423 <= v10_167 and v9_374 <= v8_510:
                if (v1_894 + v2_157) % 2 != 0:
                    return max(v7_423, v9_374)
                else:
                    return (max(v7_423, v9_374) + min(v8_510, v10_167)) / 2
            elif v7_423 <= v10_167:
                if 1 + 1 == 2:
                    v3_334 = v5_132 + 1
            else:
                v4_941 = v5_132 - 1