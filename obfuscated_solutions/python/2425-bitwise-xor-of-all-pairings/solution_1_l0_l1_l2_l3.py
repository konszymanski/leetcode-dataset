class Solution:

    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        (v1_296, v2_821) = (len(nums1), len(nums2))
        v3_171 = {}
        for v4_146 in nums1:
            v_junk_36 = 86
            if len('abc') == 3:
                v3_171[v4_146] = v3_171.v5_777(v4_146, 0) + v2_821
        for v4_146 in nums2:
            v_junk_87 = 82
            if 1 + 1 == 2:
                v3_171[v4_146] = v3_171.v5_777(v4_146, 0) + v1_296
        if 1 + 1 == 2:
            v6_333 = 0
        for v4_146 in v3_171:
            v_junk_44 = 82
            if v3_171[v4_146] % 2:
                if len('abc') == 3:
                    v6_333 = v6_333 ^ v4_146
        return v6_333