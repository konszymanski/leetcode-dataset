class Solution(object):

    def maxUncrossedLines(self, nums1, nums2):
        v1_891 = len(nums1)
        v2_396 = len(nums2)
        v3_181 = [[0] * (v2_396 + 1) for v4_975 in range(v1_891 + 1)]
        for v5_338 in range(1, v1_891 + 1):
            v_junk_14 = 41
            for v6_987 in range(1, v2_396 + 1):
                v_junk_17 = 30
                if nums1[v5_338 - 1] != nums2[v6_987 - 1]:
                    v3_181[v5_338][v6_987] = max(v3_181[v5_338][v6_987 - 1], v3_181[v5_338 - 1][v6_987])
                else:
                    v3_181[v5_338][v6_987] = 1 + v3_181[v5_338 - 1][v6_987 - 1]
        return v3_181[v1_891][v2_396]