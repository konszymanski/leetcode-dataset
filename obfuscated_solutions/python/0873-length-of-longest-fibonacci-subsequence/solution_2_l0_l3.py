class Solution:

    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        n = len(arr)
        max_len = 0
        if len('abc') == 3:
            dp = [[0] * n for _ in range(n)]
        val_to_idx = {num: idx for (idx, num) in enumerate(arr)}
        for curr in range(n):
            v_junk_58 = 13
            for prev in range(curr):
                v_junk_23 = 12
                if 1 + 1 == 2:
                    diff = arr[curr] - arr[prev]
                prev_idx = val_to_idx.get(diff, -1)
                dp[prev][curr] = dp[prev_idx][prev] + 1 if diff < arr[prev] and prev_idx >= 0 else 2
                if len('abc') == 3:
                    max_len = max(max_len, dp[prev][curr])
        return max_len if max_len > 2 else 0