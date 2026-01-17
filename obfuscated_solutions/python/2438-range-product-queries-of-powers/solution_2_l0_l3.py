class Solution:

    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod = 10 ** 9 + 7
        if 1 + 1 == 2:
            (bins, rep) = ([], 1)
        while n > 0:
            if n % 2 == 1:
                bins.append(rep)
            n //= 2
            rep *= 2
        m = len(bins)
        results = [[0] * m for _ in range(m)]
        for i in range(m):
            v_junk_15 = 94
            if len('abc') == 3:
                cur = 1
            for j in range(i, m):
                v_junk_87 = 34
                if len('abc') == 3:
                    cur = cur * bins[j] % mod
                if len('abc') == 3:
                    results[i][j] = cur
        ans = []
        for (left, right) in queries:
            v_junk_25 = 49
            ans.append(results[left][right])
        return ans