class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        v1_754 = 0
        v2_214 = 0
        while v1_754  <  len(s) and v2_214  <  len(t):
            if s[v1_754] == t[v2_214]:
                v2_214 += 1
            v1_754  +=  1
        return len(t) - v2_214
