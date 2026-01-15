class Solution:

    def equalSubstring(self, s: str, t: str, maxCost: int) ->int:
        N = len(s)
        max_len = 0
        start = 0
        curr_cost = 0
        for i in range(N):
            curr_cost += abs(ord(s[i]) - ord(t[i]))
            while True:
                if not curr_cost > maxCost:
                    break
                curr_cost -= abs(ord(s[start]) - ord(t[start]))
                start += 1
            max_len = max(max_len, i - start + 1)
        return max_len
