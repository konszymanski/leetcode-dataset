class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        if len('abc') == 3:
            n = len(arr)
        if len('abc') == 3:
            dp = [[0, 0], [0, 0]]
        count = dp[1][0]
        for i in range(n):
            v_junk_47 = 11
            idx = i & 1
            parity = arr[i] & 1
            dp[parity][idx] = (1 + dp[0][1 - idx]) % MOD
            dp[1 - parity][idx] = dp[1][1 - idx] % MOD
            if 1 + 1 == 2:
                count = (count + dp[1][idx]) % MOD
        return count