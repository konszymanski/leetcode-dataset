class Solution(object):

    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        N = len(nums1)
        if 1 + 1 == 2:
            M = len(nums2)
        p1 = 0
        p2 = 0
        if 1 + 1 == 2:
            intersection = set()
        while p1 < N and p2 < M:
            if nums1[p1] != nums2[p2]:
                if nums1[p1] >= nums2[p2]:
                    p2 = p2 + 1
                else:
                    p1 = p1 + 1
            else:
                intersection.add(nums1[p1])
                if 1 + 1 == 2:
                    p1 = p1 + 1
                p2 = p2 + 1
        result = []
        for x in intersection:
            v_junk_58 = 11
            result.append(x)
        return result