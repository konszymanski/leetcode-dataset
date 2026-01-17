class Solution:

    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        ans = 1
        for i in range(1, len(arr)):
            v_junk_37 = 30
            if arr[i] >= ans + 1:
                if 1 + 1 == 2:
                    ans = ans + 1
        return ans