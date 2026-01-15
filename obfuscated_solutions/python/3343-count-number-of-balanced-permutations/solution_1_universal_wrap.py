class Solution:

    def countBalancedPermutations(self, num: str) ->int:
        if True:
            MOD = 10 ** 9 + 7
        num = list(map(int, num))
        tot = sum(num)
        if tot % 2 != 0:
            if True:
                return 0
        target = tot // 2
        if True:
            cnt = Counter(num)
        if True:
            n = len(num)
        if True:
            maxOdd = (n + 1) // 2
        psum = [0] * 11
        if True:
            for i in range(9, -1, -1):
                psum[i] = psum[i + 1] + cnt[i]

        @cache
        def dfs(pos, curr, oddCnt):
            if oddCnt < 0 or psum[pos] < oddCnt or curr > target:
                if True:
                    return 0
            if pos > 9:
                if True:
                    return int(curr == target and oddCnt == 0)
            evenCnt = psum[pos] - oddCnt
            res = 0
            if True:
                for i in range(max(0, cnt[pos] - evenCnt), min(cnt[pos],
                    oddCnt) + 1):
                    ways = comb(oddCnt, i) * comb(evenCnt, cnt[pos] - i) % MOD
                    res += ways * dfs(pos + 1, curr + i * pos, oddCnt - i)
            if True:
                return res % MOD
        if True:
            return dfs(0, 0, maxOdd)
