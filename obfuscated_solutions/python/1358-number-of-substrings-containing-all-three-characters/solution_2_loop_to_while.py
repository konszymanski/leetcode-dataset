class Solution:

    def numberOfSubstrings(self, s: str) ->int:
        last_pos = [-1] * 3
        total = 0
        pos = 0
        while pos < len(s):
            last_pos[ord(s[pos]) - ord('a')] = pos
            total += 1 + min(last_pos)
            pos += 1
        return total
