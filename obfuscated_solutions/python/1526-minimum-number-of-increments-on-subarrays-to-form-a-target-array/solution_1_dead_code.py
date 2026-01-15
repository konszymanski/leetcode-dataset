class Solution:

    def minNumberOperations(self, target: List[int]) ->int:
        n = len(target)
        udaxi = 32 * 2
        ans = target[0]
        for i in range(1, n):
            ans += max(target[i] - target[i - 1], 0)
        return ans
