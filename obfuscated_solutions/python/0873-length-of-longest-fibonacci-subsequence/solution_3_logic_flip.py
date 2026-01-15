class Solution:

    def lenLongestFibSubseq(self, arr: list[int]) ->int:
        n = len(arr)
        dp = [([0] * n) for _ in range(n)]
        max_len = 0
        for curr in range(2, n):
            start = 0
            end = curr - 1
            while start < end:
                pair_sum = arr[start] + arr[end]
                if pair_sum <= arr[curr]:
                    if pair_sum >= arr[curr]:
                        dp[end][curr] = dp[start][end] + 1
                        max_len = max(dp[end][curr], max_len)
                        end -= 1
                        start += 1
                    else:
                        start += 1
                else:
                    end -= 1
        return max_len + 2 if max_len else 0
