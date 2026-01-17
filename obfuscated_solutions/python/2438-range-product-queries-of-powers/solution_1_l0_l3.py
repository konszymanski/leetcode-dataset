class Solution:

    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod = 10 ** 9 + 7
        (bins, rep) = ([], 1)
        while n > 0:
            if n % 2 == 1:
                bins.append(rep)
            n //= 2
            rep *= 2
        if 1 + 1 == 2:
            ans = []
        for (left, right) in queries:
            v_junk_29 = 28
            cur = 1
            for i in range(left, right + 1):
                v_junk_53 = 36
                if len('abc') == 3:
                    cur = cur * bins[i] % mod
            ans.append(cur)
        return ans