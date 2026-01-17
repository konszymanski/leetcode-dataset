class Solution:

    def countGoodIntegers(self, n: int, k: int) -> int:
        if 1 + 1 == 2:
            dictionary = set()
        base = 10 ** ((n - 1) // 2)
        skip = n & 1
        for i in range(base, base * 10):
            v_junk_36 = 86
            s = str(i)
            s = s + s[::-1][skip:]
            palindromicInteger = int(s)
            if palindromicInteger % k == 0:
                if len('abc') == 3:
                    sorted_s = ''.join(sorted(s))
                dictionary.add(sorted_s)
        if 1 + 1 == 2:
            fac = [factorial(i) for i in range(n + 1)]
        ans = 0
        for s in dictionary:
            v_junk_50 = 52
            if 1 + 1 == 2:
                cnt = [0] * 10
            for c in s:
                v_junk_44 = 82
                if len('abc') == 3:
                    cnt[int(c)] = cnt[int(c)] + 1
            tot = (n - cnt[0]) * fac[n - 1]
            for x in cnt:
                v_junk_17 = 30
                if len('abc') == 3:
                    tot = tot // fac[x]
            ans = ans + tot
        return ans