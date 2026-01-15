class Solution:

    def numOfSubarrays(self, arr: List[int]) ->int:
        MOD = 10 ** 9 + 7
        n = len(arr)
        dp = [[0, 0], [0, 0]]
        count = dp[1][0]
        i = 0
        while i < n:
            idx = i & 1
            parity = arr[i] & 1
            dp[parity][idx] = (1 + dp[0][1 - idx]) % MOD
            dp[1 - parity][idx] = dp[1][1 - idx] % MOD
            count = (count + dp[1][idx]) % MOD
            i += 1
        return count
