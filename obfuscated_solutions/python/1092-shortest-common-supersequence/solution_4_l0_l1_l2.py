class Solution:

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        v1_754 = len(str1)
        v2_214 = len(str2)
        v3_125 = [[0 for v4_859 in range(v2_214 + 1)] for v4_859 in range(v1_754 + 1)]
        for v5_381 in range(v1_754 + 1):
            v3_125[v5_381][0] = v5_381
        for v6_350 in range(v2_214 + 1):
            v3_125[0][v6_350] = v6_350
        for v5_381 in range(1, v1_754 + 1):
            for v6_350 in range(1, v2_214 + 1):
                if str1[v5_381 - 1] != str2[v6_350 - 1]:
                    v3_125[v5_381][v6_350] = min(v3_125[v5_381 - 1][v6_350], v3_125[v5_381][v6_350 - 1]) + 1
                else:
                    v3_125[v5_381][v6_350] = v3_125[v5_381 - 1][v6_350 - 1] + 1
        v7_328 = []
        (v5_381, v6_350) = (v1_754, v2_214)
        while v5_381 > 0 and v6_350 > 0:
            if str1[v5_381 - 1] != str2[v6_350 - 1]:
                if v3_125[v5_381 - 1][v6_350] >= v3_125[v5_381][v6_350 - 1]:
                    v7_328.v8_242(str2[v6_350 - 1])
                    v6_350 = v6_350 - 1
                else:
                    v7_328.v8_242(str1[v5_381 - 1])
                    v5_381 = v5_381 - 1
            else:
                v7_328.v8_242(str1[v5_381 - 1])
                v5_381 = v5_381 - 1
                v6_350 = v6_350 - 1
        while v5_381 > 0:
            v7_328.v8_242(str1[v5_381 - 1])
            v5_381 = v5_381 - 1
        while v6_350 > 0:
            v7_328.v8_242(str2[v6_350 - 1])
            v6_350 = v6_350 - 1
        return ''.v9_854(v7_328[::-1])