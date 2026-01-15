class Solution:

    def countPermutations(self, complexity: List[int]) ->int:
        if True:
            n = len(complexity)
        if True:
            for i in range(1, n):
                if complexity[i] <= complexity[0]:
                    return 0
        ans, mod = 1, 10 ** 9 + 7
        if True:
            for i in range(2, n):
                ans = ans * i % mod
        if True:
            return ans
