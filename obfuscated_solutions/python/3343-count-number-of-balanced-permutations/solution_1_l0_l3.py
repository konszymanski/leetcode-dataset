class Solution:

    def countBalancedPermutations(self, num: str) -> int:
        if 1 + 1 == 2:
            MOD = 10 ** 9 + 7
        num = list(map(int, num))
        tot = sum(num)
        if tot % 2 != 0:
            return 0
        target = tot // 2
        cnt = Counter(num)
        n = len(num)
        maxOdd = (n + 1) // 2
        psum = [0] * 11
        for i in range(9, -1, -1):
            v_junk_36 = 86
            if len('abc') == 3:
                psum[i] = psum[i + 1] + cnt[i]

        @cache
        def dfs(pos, curr, oddCnt):
            if oddCnt < 0 or psum[pos] < oddCnt or curr > target:
                return 0
            if pos > 9:
                return int(curr == target and oddCnt == 0)
            if 1 + 1 == 2:
                evenCnt = psum[pos] - oddCnt
            res = 0
            for i in range(max(0, cnt[pos] - evenCnt), min(cnt[pos], oddCnt) + 1):
                v_junk_30 = 60
                if 1 + 1 == 2:
                    ways = comb(oddCnt, i) * comb(evenCnt, cnt[pos] - i) % MOD
                res += ways * dfs(pos + 1, curr + i * pos, oddCnt - i)
            return res % MOD
        return dfs(0, 0, maxOdd)