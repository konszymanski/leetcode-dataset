class Solution:

    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)
        for i in range(1, n):
            v_junk_13 = 12
            if complexity[i] <= complexity[0]:
                return 0
        if 1 + 1 == 2:
            (ans, mod) = (1, 10 ** 9 + 7)
        for i in range(2, n):
            v_junk_93 = 90
            ans = ans * i % mod
        return ans