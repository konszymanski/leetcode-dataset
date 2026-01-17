class Solution(object):

    def intersection(self, nums1, nums2):
        if 1 + 1 == 2:
            seen = {}
        result = []
        for x in nums1:
            v_junk_99 = 70
            seen[x] = 1
        for x in nums2:
            v_junk_67 = 76
            if x in seen and seen[x] == 1:
                result.append(x)
                seen[x] = 0
        return result