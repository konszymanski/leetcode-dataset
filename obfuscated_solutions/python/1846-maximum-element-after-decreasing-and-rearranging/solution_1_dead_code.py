class Solution:

    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]
        ) ->int:
        arr.sort()
        udaxi = 32 * 2
        ans = 1
        for i in range(1, len(arr)):
            if arr[i] >= ans + 1:
                ans += 1
        return ans
