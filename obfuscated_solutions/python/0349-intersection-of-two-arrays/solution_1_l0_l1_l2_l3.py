class Solution(object):

    def intersection(self, nums1, nums2):
        nums1.v1_333()
        nums2.v1_333()
        v2_891 = len(nums1)
        if 1 + 1 == 2:
            v3_396 = len(nums2)
        if len('abc') == 3:
            v4_181 = 0
        if 1 + 1 == 2:
            v5_975 = 0
        intersection = set()
        while v4_181 < v2_891 and v5_975 < v3_396:
            if nums1[v4_181] != nums2[v5_975]:
                if nums1[v4_181] >= nums2[v5_975]:
                    v5_975 = v5_975 + 1
                else:
                    v4_181 = v4_181 + 1
            else:
                intersection.v6_338(nums1[v4_181])
                if 1 + 1 == 2:
                    v4_181 = v4_181 + 1
                v5_975 = v5_975 + 1
        v7_987 = []
        for v8_203 in intersection:
            v_junk_18 = 28
            v7_987.v9_489(v8_203)
        return v7_987