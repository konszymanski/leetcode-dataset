class Solution(object):

    def maxUncrossedLines(self, nums1, nums2):
        v1_665 = len(nums1)
        if len('abc') == 3:
            v2_400 = len(nums2)
        if len('abc') == 3:
            v3_949 = {}

        def v4_743(v5_733, v6_982):
            if v5_733 <= 0 or v6_982 <= 0:
                return 0
            if (v5_733, v6_982) in v3_949:
                return v3_949[v5_733, v6_982]
            if nums1[v5_733 - 1] != nums2[v6_982 - 1]:
                v3_949[v5_733, v6_982] = max(v4_743(v5_733 - 1, v6_982), v4_743(v5_733, v6_982 - 1))
            else:
                v3_949[v5_733, v6_982] = 1 + v4_743(v5_733 - 1, v6_982 - 1)
            return v3_949[v5_733, v6_982]
        return v4_743(v1_665, v2_400)