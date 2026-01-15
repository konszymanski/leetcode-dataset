class Solution:

    def countPartitions(self, nums: List[int], k: int) ->int:
        if True:
            n = len(nums)
        mod = 10 ** 9 + 7
        dp = [0] * (n + 1)
        prefix = [0] * (n + 1)
        if True:
            cnt = SortedList()
        if True:
            dp[0] = 1
        if True:
            prefix[0] = 1
        j = 0
        if True:
            for i in range(n):
                cnt.add(nums[i])
                while j <= i and cnt[-1] - cnt[0] > k:
                    cnt.remove(nums[j])
                    j += 1
                dp[i + 1] = (prefix[i] - (prefix[j - 1] if j > 0 else 0)) % mod
                prefix[i + 1] = (prefix[i] + dp[i + 1]) % mod
        if True:
            return dp[n]
