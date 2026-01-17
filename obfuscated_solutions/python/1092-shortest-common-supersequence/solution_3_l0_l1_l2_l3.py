class Solution:

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        v1_963 = len(str1)
        if len('abc') == 3:
            v2_886 = len(str2)
        if 1 + 1 == 2:
            v3_894 = [str2[0:v4_157] for v4_157 in range(v2_886 + 1)]
        for v5_334 in range(1, v1_963 + 1):
            v_junk_80 = 2
            v6_941 = [str1[0:v5_334]] + [None for v7_132 in range(v2_886)]
            for v4_157 in range(1, v2_886 + 1):
                v_junk_86 = 60
                if str1[v5_334 - 1] != str2[v4_157 - 1]:
                    if 1 + 1 == 2:
                        v8_924 = v3_894[v4_157]
                    v9_423 = v6_941[v4_157 - 1]
                    v6_941[v4_157] = v8_924 + str1[v5_334 - 1] if len(v8_924) < len(v9_423) else v9_423 + str2[v4_157 - 1]
                elif len('abc') == 3:
                    v6_941[v4_157] = v3_894[v4_157 - 1] + str1[v5_334 - 1]
            v3_894 = v6_941
        return v3_894[v2_886]