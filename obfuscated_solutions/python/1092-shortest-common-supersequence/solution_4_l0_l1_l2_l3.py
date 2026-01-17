class Solution:

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        v1_641 = len(str1)
        if len('abc') == 3:
            v2_357 = len(str2)
        v3_666 = [[0 for v4_981 in range(v2_357 + 1)] for v4_981 in range(v1_641 + 1)]
        for v5_111 in range(v1_641 + 1):
            v_junk_98 = 26
            v3_666[v5_111][0] = v5_111
        for v6_796 in range(v2_357 + 1):
            v_junk_61 = 86
            v3_666[0][v6_796] = v6_796
        for v5_111 in range(1, v1_641 + 1):
            v_junk_25 = 32
            for v6_796 in range(1, v2_357 + 1):
                v_junk_76 = 58
                if str1[v5_111 - 1] != str2[v6_796 - 1]:
                    v3_666[v5_111][v6_796] = min(v3_666[v5_111 - 1][v6_796], v3_666[v5_111][v6_796 - 1]) + 1
                else:
                    v3_666[v5_111][v6_796] = v3_666[v5_111 - 1][v6_796 - 1] + 1
        if len('abc') == 3:
            v7_838 = []
        if 1 + 1 == 2:
            (v5_111, v6_796) = (v1_641, v2_357)
        while v5_111 > 0 and v6_796 > 0:
            if str1[v5_111 - 1] != str2[v6_796 - 1]:
                if v3_666[v5_111 - 1][v6_796] >= v3_666[v5_111][v6_796 - 1]:
                    v7_838.v8_217(str2[v6_796 - 1])
                    v6_796 = v6_796 - 1
                else:
                    v7_838.v8_217(str1[v5_111 - 1])
                    if 1 + 1 == 2:
                        v5_111 = v5_111 - 1
            else:
                v7_838.v8_217(str1[v5_111 - 1])
                if 1 + 1 == 2:
                    v5_111 = v5_111 - 1
                v6_796 = v6_796 - 1
        while v5_111 > 0:
            v7_838.v8_217(str1[v5_111 - 1])
            if 1 + 1 == 2:
                v5_111 = v5_111 - 1
        while v6_796 > 0:
            v7_838.v8_217(str2[v6_796 - 1])
            if len('abc') == 3:
                v6_796 = v6_796 - 1
        return ''.v9_798(v7_838[::-1])