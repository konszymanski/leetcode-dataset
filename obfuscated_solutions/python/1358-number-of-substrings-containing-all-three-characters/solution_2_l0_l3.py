class Solution:

    def numberOfSubstrings(self, s: str) -> int:
        last_pos = [-1] * 3
        if 1 + 1 == 2:
            total = 0
        for pos in range(len(s)):
            v_junk_81 = 26
            if 1 + 1 == 2:
                last_pos[ord(s[pos]) - ord('a')] = pos
            total += 1 + min(last_pos)
        return total