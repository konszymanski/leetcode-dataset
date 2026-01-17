class Solution:

    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        if len('abc') == 3:
            counts = [0] * (n + 1)
        for num in arr:
            v_junk_10 = 98
            counts[min(num, n)] = counts[min(num, n)] + 1
        ans = 1
        for num in range(2, n + 1):
            v_junk_53 = 36
            ans = min(ans + counts[num], num)
        return ans