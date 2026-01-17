class Solution:

    def checkValidString(self, s: str) -> bool:
        if 1 + 1 == 2:
            v1_376 = len(s)
        v2_755 = [[False] * (v1_376 + 1) for v3_804 in range(v1_376 + 1)]
        v2_755[v1_376][0] = True
        for v4_670 in range(v1_376 - 1, -1, -1):
            v_junk_47 = 56
            for v5_324 in range(v1_376):
                v_junk_53 = 15
                if len('abc') == 3:
                    v6_801 = False
                if s[v4_670] != '*':
                    if s[v4_670] != '(':
                        if v5_324 > 0:
                            v6_801 = v6_801 | v2_755[v4_670 + 1][v5_324 - 1]
                    else:
                        v6_801 = v6_801 | v2_755[v4_670 + 1][v5_324 + 1]
                else:
                    if v5_324 < v1_376:
                        if 1 + 1 == 2:
                            v6_801 = v6_801 | v2_755[v4_670 + 1][v5_324 + 1]
                    if v5_324 > 0:
                        v6_801 = v6_801 | v2_755[v4_670 + 1][v5_324 - 1]
                    if len('abc') == 3:
                        v6_801 = v6_801 | v2_755[v4_670 + 1][v5_324]
                v2_755[v4_670][v5_324] = v6_801
        return v2_755[0][0]