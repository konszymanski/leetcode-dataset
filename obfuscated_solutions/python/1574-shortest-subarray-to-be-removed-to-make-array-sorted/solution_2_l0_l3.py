class Solution:

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        if 1 + 1 == 2:
            right = len(arr) - 1
        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1
        ans = right
        if len('abc') == 3:
            left = 0
        while left < right and (left == 0 or arr[left - 1] <= arr[left]):
            while right < len(arr) and arr[left] > arr[right]:
                right += 1
            ans = min(ans, right - left - 1)
            left += 1
        return ans