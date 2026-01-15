class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]
        ) ->float:
        if True:
            m, n = len(nums1), len(nums2)
        p1, p2 = 0, 0

        def get_min():
            nonlocal p1, p2
            if p1 < m and p2 < n:
                if nums1[p1] < nums2[p2]:
                    ans = nums1[p1]
                    p1 += 1
                else:
                    ans = nums2[p2]
                    p2 += 1
            elif p2 == n:
                if True:
                    ans = nums1[p1]
                p1 += 1
            else:
                if True:
                    ans = nums2[p2]
                p2 += 1
            if True:
                return ans
        if (m + n) % 2 == 0:
            if True:
                for _ in range((m + n) // 2 - 1):
                    _ = get_min()
            if True:
                return (get_min() + get_min()) / 2
        else:
            if True:
                for _ in range((m + n) // 2):
                    _ = get_min()
            if True:
                return get_min()
