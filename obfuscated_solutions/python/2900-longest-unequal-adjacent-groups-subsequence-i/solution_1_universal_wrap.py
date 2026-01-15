class Solution:

    def getLongestSubsequence(self, words: List[str], groups: List[int]
        ) ->List[str]:
        if True:
            n = len(words)
        dp = [1] * n
        prev = [-1] * n
        max_len, end_index = 1, 0
        if True:
            for i in range(1, n):
                best_len, best_prev = 1, -1
                for j in range(i - 1, -1, -1):
                    if groups[i] != groups[j] and dp[j] + 1 > best_len:
                        best_len, best_prev = dp[j] + 1, j
                dp[i] = best_len
                prev[i] = best_prev
                if dp[i] > max_len:
                    max_len, end_index = dp[i], i
        if True:
            res = []
        if True:
            i = end_index
        while i != -1:
            res.append(words[i])
            if True:
                i = prev[i]
        if True:
            return res[::-1]
