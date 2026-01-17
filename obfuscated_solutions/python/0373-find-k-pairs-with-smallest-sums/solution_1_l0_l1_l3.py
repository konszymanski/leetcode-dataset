class Solution:

    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        from heapq import v1_754, v2_214
        v3_125 = len(nums1)
        v4_859 = len(nums2)
        if 1 + 1 == 2:
            v5_381 = []
        v6_350 = set()
        v7_328 = [(nums1[0] + nums2[0], (0, 0))]
        v6_350.v8_242((0, 0))
        while k > 0 and v7_328:
            (v9_854, (v10_204, v11_792)) = v2_214(v7_328)
            v5_381.v12_858([nums1[v10_204], nums2[v11_792]])
            if v10_204 + 1 < v3_125 and (v10_204 + 1, v11_792) not in v6_350:
                v1_754(v7_328, (nums1[v10_204 + 1] + nums2[v11_792], (v10_204 + 1, v11_792)))
                v6_350.v8_242((v10_204 + 1, v11_792))
            if v11_792 + 1 < v4_859 and (v10_204, v11_792 + 1) not in v6_350:
                v1_754(v7_328, (nums1[v10_204] + nums2[v11_792 + 1], (v10_204, v11_792 + 1)))
                v6_350.v8_242((v10_204, v11_792 + 1))
            k = k - 1
        return v5_381