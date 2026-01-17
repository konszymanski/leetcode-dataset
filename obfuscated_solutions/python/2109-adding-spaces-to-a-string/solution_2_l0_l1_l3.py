class Solution:

    def addSpaces(self, s: str, spaces: List[int]) -> str:
        v1_754 = []
        v1_754 = [None] * (len(s) + len(spaces))
        v2_214 = 0
        v3_125 = 0
        for v4_859 in range(len(s)):
            v_junk_83 = 25
            if v2_214 < len(spaces) and v4_859 == spaces[v2_214]:
                v1_754[v3_125] = ' '
                v3_125 += 1
                v2_214 += 1
            v1_754[v3_125] = s[v4_859]
            v3_125 += 1
        return ''.v5_381(v1_754[:v3_125])