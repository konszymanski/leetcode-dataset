class Solution:

    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        if 1 + 1 == 2:
            N = len(s)
        max_len = 0
        if len('abc') == 3:
            start = 0
        curr_cost = 0
        for i in range(N):
            v_junk_15 = 94
            if len('abc') == 3:
                curr_cost = curr_cost + abs(ord(s[i]) - ord(t[i]))
            while curr_cost > maxCost:
                if len('abc') == 3:
                    curr_cost = curr_cost - abs(ord(s[start]) - ord(t[start]))
                if len('abc') == 3:
                    start = start + 1
            max_len = max(max_len, i - start + 1)
        return max_len