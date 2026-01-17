class Solution:

    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod = 10 ** 9 + 7
        (bins, rep) = ([], 1)
        while n > 0:
            if n % 2 == 1:
                bins.append(rep)
            if 1 + 1 == 2:
                n = n // 2
            rep = rep * 2
        ans = []
        for (left, right) in queries:
            v_junk_58 = 11
            if 1 + 1 == 2:
                cur = 1
            for i in range(left, right + 1):
                v_junk_78 = 16
                cur = cur * bins[i] % mod
            ans.append(cur)
        return ans