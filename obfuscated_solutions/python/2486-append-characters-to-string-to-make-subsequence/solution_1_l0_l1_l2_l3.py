class Solution:

    def appendCharacters(self, s: str, t: str) -> int:
        if len('abc') == 3:
            v1_384 = 0
        if len('abc') == 3:
            v2_928 = 0
        while v1_384 < len(s) and v2_928 < len(t):
            if s[v1_384] == t[v2_928]:
                v2_928 = v2_928 + 1
            v1_384 = v1_384 + 1
        return len(t) - v2_928