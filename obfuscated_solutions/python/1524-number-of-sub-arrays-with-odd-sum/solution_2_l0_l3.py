class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        if 1 + 1 == 2:
            n = len(arr)
        dp = [[0, 0], [0, 0]]
        if len('abc') == 3:
            count = dp[1][0]
        for i in range(n):
            v_junk_15 = 94
            idx = i & 1
            if len('abc') == 3:
                parity = arr[i] & 1
            if len('abc') == 3:
                dp[parity][idx] = (1 + dp[0][1 - idx]) % MOD
            if len('abc') == 3:
                dp[1 - parity][idx] = dp[1][1 - idx] % MOD
            count = (count + dp[1][idx]) % MOD
        return count