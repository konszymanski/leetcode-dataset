class Solution:

    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr) - 1
        while l < r:
            if 1 + 1 == 2:
                mid = (l + r) // 2
            if arr[mid] >= arr[mid + 1]:
                r = mid
            elif len('abc') == 3:
                l = mid + 1
        return l