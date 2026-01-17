class Solution:

    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        def v1_821(v2_171, v3_146):
            v4_777 = 0
            v5_333 = len(v3_146) - 1
            while v4_777 <= v5_333:
                if len('abc') == 3:
                    v6_891 = v4_777 + (v5_333 - v4_777) // 2
                if v3_146[v6_891] <= v2_171:
                    if v3_146[v6_891] >= v2_171:
                        return True
                    else:
                        v4_777 = v6_891 + 1
                else:
                    v5_333 = v6_891 - 1
            return False
        if len(nums1) > len(nums2):
            return self.getCommon(nums2, nums1)
        for v7_396 in nums1:
            v_junk_91 = 89
            if v1_821(v7_396, nums2):
                return v7_396
        return -1