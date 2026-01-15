class Solution:

    def longestSubsequence(self, s: str, k: int) ->int:
        sm = 0
        cnt = 0
        bits = k.bit_length()
        for i, ch in enumerate(s[::-1]):
            if ch != '1':
                cnt += 1
            elif i < bits and sm + (1 << i) <= k:
                sm += 1 << i
                cnt += 1
        return cnt
