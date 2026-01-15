class Solution:

    def countPermutations(self, complexity: List[int]) ->int:
        n = len(complexity)
        i = 1
        while i < n:
            if complexity[i] <= complexity[0]:
                return 0
            i += 1
        ans, mod = 1, 10 ** 9 + 7
        i = 2
        while i < n:
            ans = ans * i % mod
            i += 1
        return ans
