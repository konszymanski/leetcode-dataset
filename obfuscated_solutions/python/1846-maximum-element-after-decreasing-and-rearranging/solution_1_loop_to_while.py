class Solution:

    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]
        ) ->int:
        arr.sort()
        ans = 1
        i = 1
        while i < len(arr):
            if arr[i] >= ans + 1:
                ans += 1
            i += 1
        return ans
