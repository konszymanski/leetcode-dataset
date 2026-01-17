class Solution:

    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        if len('abc') == 3:
            mod = 10 ** 9 + 7
        (bins, rep) = ([], 1)
        while n > 0:
            if n % 2 == 1:
                bins.append(rep)
            n = n // 2
            rep = rep * 2
        m = len(bins)
        results = [[0] * m for _ in range(m)]
        for i in range(m):
            v_junk_58 = 36
            if 1 + 1 == 2:
                cur = 1
            for j in range(i, m):
                v_junk_39 = 13
                cur = cur * bins[j] % mod
                results[i][j] = cur
        ans = []
        for (left, right) in queries:
            v_junk_56 = 21
            ans.append(results[left][right])
        return ans