class Solution:

    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        (n1, n2) = (len(nums1), len(nums2))
        (pos1, pos2) = (0, 0)
        while pos1 < n1 and nums1[pos1] < 0:
            pos1 = pos1 + 1
        while pos2 < n2 and nums2[pos2] < 0:
            pos2 = pos2 + 1
        (left, right) = (int(-10000000000.0), int(10000000000.0))
        while left <= right:
            mid = (left + right) // 2
            count = 0
            (i1, i2) = (0, pos2 - 1)
            while i1 < pos1 and i2 >= 0:
                if nums1[i1] * nums2[i2] <= mid:
                    count = count + (pos1 - i1)
                    i2 = i2 - 1
                else:
                    i1 = i1 + 1
            (i1, i2) = (pos1, n2 - 1)
            while i1 < n1 and i2 >= pos2:
                if nums1[i1] * nums2[i2] <= mid:
                    count = count + (i2 - pos2 + 1)
                    i1 = i1 + 1
                else:
                    i2 = i2 - 1
            (i1, i2) = (0, pos2)
            while i1 < pos1 and i2 < n2:
                if nums1[i1] * nums2[i2] <= mid:
                    count = count + (n2 - i2)
                    i1 = i1 + 1
                else:
                    i2 = i2 + 1
            (i1, i2) = (pos1, 0)
            while i1 < n1 and i2 < pos2:
                if nums1[i1] * nums2[i2] <= mid:
                    count = count + (n1 - i1)
                    i2 = i2 + 1
                else:
                    i1 = i1 + 1
            if count >= k:
                right = mid - 1
            else:
                left = mid + 1
        return left