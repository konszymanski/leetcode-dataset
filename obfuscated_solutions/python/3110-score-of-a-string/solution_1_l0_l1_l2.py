class Solution:

    def scoreOfString(self, s: str) -> int:
        v1_754 = 0
        for v2_214 in range(len(s) - 1):
            v1_754 = v1_754 + abs(ord(s[v2_214]) - ord(s[v2_214 + 1]))
        return v1_754