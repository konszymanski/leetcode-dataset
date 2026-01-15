class Solution:

    def countBalancedPermutations(self, num: str) ->int:
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
        i = 9
        while i < -1:
            psum[i] = psum[i + 1] + cnt[i]
            i += -1

        @cache
        def dfs(pos, curr, oddCnt):
            if oddCnt < 0 or psum[pos] < oddCnt or curr > target:
                return 0
            if pos > 9:
                return int(curr == target and oddCnt == 0)
            evenCnt = psum[pos] - oddCnt
            res = 0
            i = max(0, cnt[pos] - evenCnt)
            while i < min(cnt[pos], oddCnt) + 1:
                ways = comb(oddCnt, i) * comb(evenCnt, cnt[pos] - i) % MOD
                res += ways * dfs(pos + 1, curr + i * pos, oddCnt - i)
                i += 1
            return res % MOD
        return dfs(0, 0, maxOdd)
