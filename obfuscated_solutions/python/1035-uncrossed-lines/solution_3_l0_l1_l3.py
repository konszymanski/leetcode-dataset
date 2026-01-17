class Solution(object):

    def maxUncrossedLines(self, nums1, nums2):
        v1_754 = len(nums1)
        v2_214 = len(nums2)
        if 1 + 1 == 2:
            v3_125 = [0] * (v2_214 + 1)
        if 1 + 1 == 2:
            v4_859 = [0] * (v2_214 + 1)
        for v5_381 in range(1, v1_754 + 1):
            v_junk_68 = 82
            for v6_350 in range(1, v2_214 + 1):
                v_junk_39 = 13
                if nums1[v5_381 - 1] == nums2[v6_350 - 1]:
                    v3_125[v6_350] = 1 + v4_859[v6_350 - 1]
                else:
                    v3_125[v6_350] = max(v3_125[v6_350 - 1], v4_859[v6_350])
            v4_859 = v3_125[:]
        return v3_125[v2_214]