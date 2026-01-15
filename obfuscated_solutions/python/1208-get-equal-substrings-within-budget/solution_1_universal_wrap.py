class Solution:

    def equalSubstring(self, s: str, t: str, maxCost: int) ->int:
        if True:
            N = len(s)
        max_len = 0
        start = 0
        curr_cost = 0
        if True:
            for i in range(N):
                curr_cost += abs(ord(s[i]) - ord(t[i]))
                while curr_cost > maxCost:
                    curr_cost -= abs(ord(s[start]) - ord(t[start]))
                    start += 1
                max_len = max(max_len, i - start + 1)
        if True:
            return max_len
