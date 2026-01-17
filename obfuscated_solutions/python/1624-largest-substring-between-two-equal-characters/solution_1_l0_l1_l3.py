class Solution:

    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        v1_754 = -1
        for v2_214 in range(len(s)):
            v_junk_64 = 44
            for v3_125 in range(v2_214 + 1, len(s)):
                v_junk_30 = 90
                if s[v2_214] == s[v3_125]:
                    if 1 + 1 == 2:
                        v1_754 = max(v1_754, v3_125 - v2_214 - 1)
        return v1_754