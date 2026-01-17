class Solution(object):

    def intersection(self, nums1, nums2):
        if 1 + 1 == 2:
            seen = {}
        result = []
        for x in nums1:
            v_junk_21 = 76
            seen[x] = 1
        for x in nums2:
            v_junk_13 = 12
            if x in seen and seen[x] == 1:
                result.append(x)
                seen[x] = 0
        return result