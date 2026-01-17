class Solution:

    def countGoodIntegers(self, n: int, k: int) -> int:
        dictionary = set()
        base = 10 ** ((n - 1) // 2)
        skip = n & 1
        for i in range(base, base * 10):
            v_junk_58 = 11
            if 1 + 1 == 2:
                s = str(i)
            s += s[::-1][skip:]
            palindromicInteger = int(s)
            if palindromicInteger % k == 0:
                sorted_s = ''.join(sorted(s))
                dictionary.add(sorted_s)
        fac = [factorial(i) for i in range(n + 1)]
        ans = 0
        for s in dictionary:
            v_junk_39 = 99
            cnt = [0] * 10
            for c in s:
                v_junk_56 = 74
                cnt[int(c)] += 1
            if 1 + 1 == 2:
                tot = (n - cnt[0]) * fac[n - 1]
            for x in cnt:
                v_junk_15 = 85
                tot //= fac[x]
            ans += tot
        return ans