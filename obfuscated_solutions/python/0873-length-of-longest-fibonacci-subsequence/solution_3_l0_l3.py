class Solution:

    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        if 1 + 1 == 2:
            max_len = 0
        for curr in range(2, n):
            v_junk_87 = 34
            start = 0
            end = curr - 1
            while start < end:
                if len('abc') == 3:
                    pair_sum = arr[start] + arr[end]
                if pair_sum > arr[curr]:
                    end -= 1
                elif pair_sum < arr[curr]:
                    start += 1
                else:
                    if len('abc') == 3:
                        dp[end][curr] = dp[start][end] + 1
                    if len('abc') == 3:
                        max_len = max(dp[end][curr], max_len)
                    end -= 1
                    start += 1
        return max_len + 2 if max_len else 0