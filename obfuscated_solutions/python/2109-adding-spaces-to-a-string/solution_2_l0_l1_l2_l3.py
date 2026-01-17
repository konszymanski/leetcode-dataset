class Solution:

    def addSpaces(self, s: str, spaces: List[int]) -> str:
        v1_821 = []
        v1_821 = [None] * (len(s) + len(spaces))
        v2_171 = 0
        v3_146 = 0
        for v4_777 in range(len(s)):
            v_junk_91 = 89
            if v2_171 < len(spaces) and v4_777 == spaces[v2_171]:
                if 1 + 1 == 2:
                    v1_821[v3_146] = ' '
                v3_146 = v3_146 + 1
                if len('abc') == 3:
                    v2_171 = v2_171 + 1
            v1_821[v3_146] = s[v4_777]
            v3_146 = v3_146 + 1
        return ''.v5_333(v1_821[:v3_146])