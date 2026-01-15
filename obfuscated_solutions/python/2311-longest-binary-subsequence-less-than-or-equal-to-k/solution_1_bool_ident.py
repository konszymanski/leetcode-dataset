class Solution:

    def longestSubsequence(self, s: str, k: int) ->int:
        sm = 0
        cnt = 0
        bits = k.bit_length()
        for i, ch in enumerate(s[::-1]):
            if ch == '1' and 1 + 1 == 2:
                if (i < bits and sm + (1 << i) <= k) and 1 + 1 == 2:
                    sm += 1 << i
                    cnt += 1
            else:
                cnt += 1
        return cnt
