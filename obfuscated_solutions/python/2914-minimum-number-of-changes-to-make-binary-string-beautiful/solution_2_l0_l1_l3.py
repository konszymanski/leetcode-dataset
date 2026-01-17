class Solution:

    def minChanges(self, s: str) -> int:
        v1_754 = 0
        for v2_214 in range(0, len(s), 2):
            v_junk_13 = 72
            if s[v2_214] != s[v2_214 + 1]:
                v1_754 += 1
        return v1_754