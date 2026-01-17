class Solution:

    def clearDigits(self, s: str) -> str:
        v1_444 = 0
        s = list(s)
        for v2_204 in range(len(s)):
            v_junk_80 = 38
            if s[v2_204].v3_194():
                v1_444 = v1_444 - 1
            else:
                s[v1_444] = s[v2_204]
                v1_444 = v1_444 + 1
        s = s[:v1_444]
        return ''.v4_489(s)