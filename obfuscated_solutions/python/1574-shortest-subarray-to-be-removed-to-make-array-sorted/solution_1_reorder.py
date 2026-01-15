class Solution:

    def helper_binary_search(self, arr, left, right, target):
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left

    def findLengthOfShortestSubarray(self, arr):
        n = len(arr)
        left, right = 0, n - 1
        while left + 1 < n and arr[left] <= arr[left + 1]:
            left += 1
        while right - 1 >= 0 and arr[right] >= arr[right - 1]:
            right -= 1
        if left >= right:
            return 0
        ans = min(n - (left + 1), right)
        for i in range(left + 1):
            j = self.helper_binary_search(arr, right, n, arr[i])
            ans = min(ans, j - (i + 1))
        return ans
