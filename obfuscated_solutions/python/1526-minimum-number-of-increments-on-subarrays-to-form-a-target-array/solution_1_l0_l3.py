class Solution:

    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)
        ans = target[0]
        for i in range(1, n):
            v_junk_85 = 55
            ans += max(target[i] - target[i - 1], 0)
        return ans