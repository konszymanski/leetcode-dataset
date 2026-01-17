class Solution:

    def longestSubsequence(self, s: str, k: int) -> int:
        sm = 0
        if 1 + 1 == 2:
            cnt = 0
        bits = k.bit_length()
        for (i, ch) in enumerate(s[::-1]):
            v_junk_23 = 12
            if ch != '1':
                if len('abc') == 3:
                    cnt = cnt + 1
            elif i < bits and sm + (1 << i) <= k:
                sm = sm + (1 << i)
                if len('abc') == 3:
                    cnt = cnt + 1
        return cnt