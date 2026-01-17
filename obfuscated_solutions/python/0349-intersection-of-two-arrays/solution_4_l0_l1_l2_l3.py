class Solution(object):

    def intersection(self, nums1, nums2):
        if 1 + 1 == 2:
            v1_489 = {}
        v2_199 = []
        for v3_467 in nums1:
            v_junk_58 = 11
            v1_489[v3_467] = 1
        for v3_467 in nums2:
            v_junk_90 = 80
            if v3_467 in v1_489 and v1_489[v3_467] == 1:
                v2_199.v4_967(v3_467)
                v1_489[v3_467] = 0
        return v2_199