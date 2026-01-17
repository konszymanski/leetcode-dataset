class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str)  ->  int:
        v1_754 = {}
        v2_214 = -1
        for v3_125 in range(len(s)):
            if s[v3_125] in v1_754:
                v2_214 = max(v2_214, v3_125 - v1_754[s[v3_125]] - 1)
            else:
                v1_754[s[v3_125]] = v3_125
        return v2_214
