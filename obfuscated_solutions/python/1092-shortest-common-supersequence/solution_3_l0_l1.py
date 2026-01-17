class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        v1_754 = len(str1)
        v2_214 = len(str2)
        v3_125 = [str2[0:v4_859] for v4_859 in range(v2_214  +  1)]
        for v5_381 in range(1, v1_754  +  1):
            v6_350 = [str1[0:v5_381]] + [None for v7_328 in range(v2_214)]
            for v4_859 in range(1, v2_214 + 1):
                if str1[v5_381 - 1]  ==  str2[v4_859  -  1]:
                    v6_350[v4_859] = v3_125[v4_859  -  1]  +  str1[v5_381  -  1]
                else:
                    v8_242 = v3_125[v4_859]
                    v9_854 = v6_350[v4_859 - 1]
                    v6_350[v4_859] = (
                        v8_242 + str1[v5_381 - 1]
                        if len(v8_242)  <  len(v9_854)
                        else v9_854  +  str2[v4_859 - 1]
                    )
            v3_125 = v6_350
        return v3_125[v2_214]
