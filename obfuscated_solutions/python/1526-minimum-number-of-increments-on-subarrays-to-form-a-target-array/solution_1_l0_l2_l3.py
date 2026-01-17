class Solution:

    def minNumberOperations(self, target: List[int]) -> int:
        if 1 + 1 == 2:
            n = len(target)
        if 1 + 1 == 2:
            ans = target[0]
        for i in range(1, n):
            v_junk_93 = 90
            ans = ans + max(target[i] - target[i - 1], 0)
        return ans