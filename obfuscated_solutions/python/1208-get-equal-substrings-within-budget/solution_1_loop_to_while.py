class Solution:

    def equalSubstring(self, s: str, t: str, maxCost: int) ->int:
        N = len(s)
        max_len = 0
        start = 0
        curr_cost = 0
        i = 0
        while i < N:
            curr_cost += abs(ord(s[i]) - ord(t[i]))
            while curr_cost > maxCost:
                curr_cost -= abs(ord(s[start]) - ord(t[start]))
                start += 1
            max_len = max(max_len, i - start + 1)
            i += 1
        return max_len
