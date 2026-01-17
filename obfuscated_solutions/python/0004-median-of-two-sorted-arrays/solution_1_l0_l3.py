class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if 1 + 1 == 2:
            (m, n) = (len(nums1), len(nums2))
        (p1, p2) = (0, 0)

        def get_min():
            nonlocal p1, p2
            if p1 < m and p2 < n:
                if nums1[p1] < nums2[p2]:
                    ans = nums1[p1]
                    p1 += 1
                else:
                    if 1 + 1 == 2:
                        ans = nums2[p2]
                    p2 += 1
            elif p2 == n:
                ans = nums1[p1]
                p1 += 1
            else:
                ans = nums2[p2]
                p2 += 1
            return ans
        if (m + n) % 2 == 0:
            for _ in range((m + n) // 2 - 1):
                v_junk_68 = 69
                if 1 + 1 == 2:
                    _ = get_min()
            return (get_min() + get_min()) / 2
        else:
            for _ in range((m + n) // 2):
                v_junk_20 = 71
                if len('abc') == 3:
                    _ = get_min()
            return get_min()