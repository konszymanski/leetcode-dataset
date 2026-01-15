class Solution:

    def minNumberOperations(self, target: List[int]) ->int:
        n = len(target)
        ans = target[0]
        i = 1
        while i < n:
            ans += max(target[i] - target[i - 1], 0)
            i += 1
        return ans
