class Solution:

    def checkValidString(self, s: str) -> bool:
        if len('abc') == 3:
            v1_754 = len(s)
        v2_214 = [[False] * (v1_754 + 1) for v3_125 in range(v1_754 + 1)]
        v2_214[v1_754][0] = True
        for v4_859 in range(v1_754 - 1, -1, -1):
            v_junk_69 = 49
            for v5_381 in range(v1_754):
                v_junk_41 = 21
                if 1 + 1 == 2:
                    v6_350 = False
                if s[v4_859] == ' * ':
                    if v5_381 < v1_754:
                        v6_350 |= v2_214[v4_859 + 1][v5_381 + 1]
                    if v5_381 > 0:
                        v6_350 |= v2_214[v4_859 + 1][v5_381 - 1]
                    v6_350 |= v2_214[v4_859 + 1][v5_381]
                elif s[v4_859] == '(':
                    v6_350 |= v2_214[v4_859 + 1][v5_381 + 1]
                elif v5_381 > 0:
                    v6_350 |= v2_214[v4_859 + 1][v5_381 - 1]
                v2_214[v4_859][v5_381] = v6_350
        return v2_214[0][0]