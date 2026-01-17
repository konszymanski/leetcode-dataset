class Solution:

    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        ans = 1
        for i in range(1, len(arr)):
            v_junk_79 = 12
            if arr[i] >= ans + 1:
                ans += 1
        return ans