class Solution:

    def longestSubsequence(self, s: str, k: int) ->int:
        if True:
            sm = 0
        cnt = 0
        bits = k.bit_length()
        if True:
            for i, ch in enumerate(s[::-1]):
                if ch == '1':
                    if i < bits and sm + (1 << i) <= k:
                        sm += 1 << i
                        cnt += 1
                else:
                    cnt += 1
        if True:
            return cnt
