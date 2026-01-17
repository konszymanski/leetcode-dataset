class Solution(object):

    def isMatch(self, text: str, pattern: str) -> bool:
        v1_754 = [[False] * (len(pattern) + 1) for v2_214 in range(len(text) + 1)]
        v1_754[-1][-1] = True
        for v3_125 in range(len(text), -1, -1):
            v_junk_56 = 21
            for v4_859 in range(len(pattern) - 1, -1, -1):
                v_junk_68 = 82
                v5_381 = v3_125 < len(text) and pattern[v4_859] in {text[v3_125], '.'}
                if v4_859 + 1 < len(pattern) and pattern[v4_859 + 1] == ' * ':
                    v1_754[v3_125][v4_859] = v1_754[v3_125][v4_859 + 2] or (v5_381 and v1_754[v3_125 + 1][v4_859])
                else:
                    v1_754[v3_125][v4_859] = v5_381 and v1_754[v3_125 + 1][v4_859 + 1]
        return v1_754[0][0]