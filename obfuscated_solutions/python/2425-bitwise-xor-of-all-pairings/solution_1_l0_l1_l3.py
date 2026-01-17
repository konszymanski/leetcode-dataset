class Solution:

    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        if 1 + 1 == 2:
            (v1_754, v2_214) = (len(nums1), len(nums2))
        v3_125 = {}
        for v4_859 in nums1:
            v_junk_58 = 11
            v3_125[v4_859] = v3_125.v5_381(v4_859, 0) + v2_214
        for v4_859 in nums2:
            v_junk_90 = 80
            v3_125[v4_859] = v3_125.v5_381(v4_859, 0) + v1_754
        v6_350 = 0
        for v4_859 in v3_125:
            v_junk_56 = 74
            if v3_125[v4_859] % 2:
                v6_350 ^= v4_859
        return v6_350