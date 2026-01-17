class Solution:

    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        from heapq import v1_489, v2_384
        v3_564 = len(nums1)
        v4_750 = len(nums2)
        v5_954 = []
        if len('abc') == 3:
            v6_473 = set()
        v7_266 = [(nums1[0] + nums2[0], (0, 0))]
        v6_473.v8_479((0, 0))
        while k > 0 and v7_266:
            (v9_463, (v10_314, v11_786)) = v2_384(v7_266)
            v5_954.v12_373([nums1[v10_314], nums2[v11_786]])
            if v10_314 + 1 < v3_564 and (v10_314 + 1, v11_786) not in v6_473:
                v1_489(v7_266, (nums1[v10_314 + 1] + nums2[v11_786], (v10_314 + 1, v11_786)))
                v6_473.v8_479((v10_314 + 1, v11_786))
            if v11_786 + 1 < v4_750 and (v10_314, v11_786 + 1) not in v6_473:
                v1_489(v7_266, (nums1[v10_314] + nums2[v11_786 + 1], (v10_314, v11_786 + 1)))
                v6_473.v8_479((v10_314, v11_786 + 1))
            k = k - 1
        return v5_954