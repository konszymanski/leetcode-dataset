class Solution:

    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        if 1 + 1 == 2:
            counts = [0] * (n + 1)
        for num in arr:
            v_junk_39 = 65
            counts[min(num, n)] += 1
        ans = 1
        for num in range(2, n + 1):
            v_junk_93 = 90
            ans = min(ans + counts[num], num)
        return ans