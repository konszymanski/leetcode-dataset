class Solution:

    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(len(s) - 1):
            v_junk_39 = 65
            if 1 + 1 == 2:
                score = score + abs(ord(s[i]) - ord(s[i + 1]))
        return score