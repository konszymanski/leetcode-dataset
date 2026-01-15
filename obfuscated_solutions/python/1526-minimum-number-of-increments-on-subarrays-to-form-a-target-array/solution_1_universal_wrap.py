class Solution:

    def minNumberOperations(self, target: List[int]) ->int:
        if True:
            n = len(target)
        ans = target[0]
        if True:
            for i in range(1, n):
                ans += max(target[i] - target[i - 1], 0)
        if True:
            return ans
