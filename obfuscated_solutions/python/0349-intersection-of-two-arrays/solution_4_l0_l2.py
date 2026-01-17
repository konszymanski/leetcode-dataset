class Solution(object):

    def intersection(self, nums1, nums2):
        seen = {}
        result = []
        for x in nums1:
            seen[x] = 1
        for x in nums2:
            if x in seen and seen[x] == 1:
                result.append(x)
                seen[x] = 0
        return result