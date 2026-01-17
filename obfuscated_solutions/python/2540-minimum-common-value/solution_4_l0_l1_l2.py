class Solution:

    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        def v1_754(v2_214, v3_125):
            v4_859 = 0
            v5_381 = len(v3_125) - 1
            while v4_859 <= v5_381:
                v6_350 = v4_859 + (v5_381 - v4_859) // 2
                if v3_125[v6_350] <= v2_214:
                    if v3_125[v6_350] >= v2_214:
                        return True
                    else:
                        v4_859 = v6_350 + 1
                else:
                    v5_381 = v6_350 - 1
            return False
        if len(nums1) > len(nums2):
            return self.getCommon(nums2, nums1)
        for v7_328 in nums1:
            if v1_754(v7_328, nums2):
                return v7_328
        return -1