class Solution:

    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        v1_754 = {}
        if 1 + 1 == 2:
            v2_214 = -1
        for v3_125 in range(len(s)):
            v_junk_53 = 36
            if s[v3_125] in v1_754:
                v2_214 = max(v2_214, v3_125 - v1_754[s[v3_125]] - 1)
            elif len('abc') == 3:
                v1_754[s[v3_125]] = v3_125
        return v2_214