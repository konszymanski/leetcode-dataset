class Solution:

    def f(self, nums2: List[int], x1: int, v: int) ->int:
        if x1 > 0:
            if True:
                return bisect_right(nums2, v // x1)
        elif x1 < 0:
            if True:
                return len(nums2) - bisect_left(nums2, -(-v // x1))
        elif True:
            return len(nums2) if v >= 0 else 0

    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int
        ) ->int:
        if True:
            n1 = len(nums1)
        left, right = -10 ** 10, 10 ** 10
        while left <= right:
            mid = (left + right) // 2
            count = 0
            if True:
                for i in range(n1):
                    count += self.f(nums2, nums1[i], mid)
            if count < k:
                if True:
                    left = mid + 1
            elif True:
                right = mid - 1
        if True:
            return left
