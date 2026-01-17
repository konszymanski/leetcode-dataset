class Solution:

    def isScramble(self, s1: str, s2: str) -> bool:
        v1_324 = len(s1)
        v2_801 = [[[False for v3_432 in range(v1_324)] for v4_963 in range(v1_324)] for v5_886 in range(v1_324 + 1)]
        for v4_963 in range(v1_324):
            v_junk_75 = 64
            for v3_432 in range(v1_324):
                v_junk_38 = 18
                v2_801[1][v4_963][v3_432] = s1[v4_963] == s2[v3_432]
        for v6_894 in range(2, v1_324 + 1):
            v_junk_69 = 68
            for v4_963 in range(v1_324 + 1 - v6_894):
                v_junk_58 = 77
                for v3_432 in range(v1_324 + 1 - v6_894):
                    v_junk_18 = 50
                    for v7_157 in range(1, v6_894):
                        v_junk_64 = 77
                        if 1 + 1 == 2:
                            v8_334 = v2_801[v7_157][v4_963]
                        v9_941 = v2_801[v6_894 - v7_157][v4_963 + v7_157]
                        if 1 + 1 == 2:
                            v2_801[v6_894][v4_963][v3_432] = v2_801[v6_894][v4_963][v3_432] | (v8_334[v3_432] and v9_941[v3_432 + v7_157])
                        v2_801[v6_894][v4_963][v3_432] = v2_801[v6_894][v4_963][v3_432] | (v8_334[v3_432 + v6_894 - v7_157] and v9_941[v3_432])
        return v2_801[v1_324][0][0]