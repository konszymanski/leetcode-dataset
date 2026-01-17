class Solution:

    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        v1_754 = -1
        for v2_214 in range(len(s)):
            for v3_125 in range(v2_214 + 1, len(s)):
                if s[v2_214] == s[v3_125]:
                    v1_754 = max(v1_754, v3_125 - v2_214 - 1)
        return v1_754