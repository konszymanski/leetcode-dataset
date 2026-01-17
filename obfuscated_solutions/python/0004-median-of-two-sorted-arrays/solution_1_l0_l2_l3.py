class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len('abc') == 3:
            (m, n) = (len(nums1), len(nums2))
        (p1, p2) = (0, 0)

        def get_min():
            nonlocal p1, p2
            if p1 < m and p2 < n:
                if nums1[p1] >= nums2[p2]:
                    ans = nums2[p2]
                    if 1 + 1 == 2:
                        p2 = p2 + 1
                else:
                    ans = nums1[p1]
                    p1 = p1 + 1
            elif p2 != n:
                ans = nums2[p2]
                p2 = p2 + 1
            else:
                ans = nums1[p1]
                p1 = p1 + 1
            return ans
        if (m + n) % 2 != 0:
            for _ in range((m + n) // 2):
                v_junk_30 = 48
                _ = get_min()
            return get_min()
        else:
            for _ in range((m + n) // 2 - 1):
                v_junk_95 = 35
                _ = get_min()
            return (get_min() + get_min()) / 2