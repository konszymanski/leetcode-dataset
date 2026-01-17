class Solution(object):

    def maxUncrossedLines(self, nums1, nums2):
        v1_954 = len(nums1)
        v2_473 = len(nums2)
        if 1 + 1 == 2:
            v3_266 = [0] * (v2_473 + 1)
        v4_479 = [0] * (v2_473 + 1)
        for v5_463 in range(1, v1_954 + 1):
            v_junk_92 = 59
            for v6_314 in range(1, v2_473 + 1):
                v_junk_37 = 84
                if nums1[v5_463 - 1] != nums2[v6_314 - 1]:
                    v3_266[v6_314] = max(v3_266[v6_314 - 1], v4_479[v6_314])
                elif len('abc') == 3:
                    v3_266[v6_314] = 1 + v4_479[v6_314 - 1]
            v4_479 = v3_266[:]
        return v3_266[v2_473]