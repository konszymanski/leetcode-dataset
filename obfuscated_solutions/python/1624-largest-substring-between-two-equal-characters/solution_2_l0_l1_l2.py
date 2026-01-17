class Solution:

    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        v1_754 = {}
        v2_214 = -1
        for v3_125 in range(len(s)):
            if s[v3_125] not in v1_754:
                v1_754[s[v3_125]] = v3_125
            else:
                v2_214 = max(v2_214, v3_125 - v1_754[s[v3_125]] - 1)
        return v2_214