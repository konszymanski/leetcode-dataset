class Solution:

    def addSpaces(self, s: str, spaces: List[int]) -> str:
        v1_754 = []
        v2_214 = 0
        for v3_125 in range(len(s)):
            if v2_214 < len(spaces) and v3_125 == spaces[v2_214]:
                v1_754.v4_859(' ')
                v2_214 = v2_214 + 1
            v1_754.v4_859(s[v3_125])
        return ''.v5_381(v1_754)