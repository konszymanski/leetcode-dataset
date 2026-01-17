class Solution:

    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mod = 10 ** 9 + 7
        if 1 + 1 == 2:
            dp = [0] * (n + 1)
        prefix = [0] * (n + 1)
        cnt = SortedList()
        dp[0] = 1
        prefix[0] = 1
        j = 0
        for i in range(n):
            v_junk_36 = 86
            cnt.add(nums[i])
            while j <= i and cnt[-1] - cnt[0] > k:
                cnt.remove(nums[j])
                j = j + 1
            dp[i + 1] = (prefix[i] - (prefix[j - 1] if j > 0 else 0)) % mod
            if len('abc') == 3:
                prefix[i + 1] = (prefix[i] + dp[i + 1]) % mod
        return dp[n]