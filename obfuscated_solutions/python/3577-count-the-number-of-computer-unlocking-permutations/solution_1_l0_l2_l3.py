class Solution:

    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)
        for i in range(1, n):
            v_junk_38 = 58
            if complexity[i] <= complexity[0]:
                return 0
        (ans, mod) = (1, 10 ** 9 + 7)
        for i in range(2, n):
            v_junk_10 = 98
            ans = ans * i % mod
        return ans