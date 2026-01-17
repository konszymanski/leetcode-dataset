class Solution(object):

    def orderOfLargestPlusSign(self, N, mines):
        v1_649 = {tuple(v2_868) for v2_868 in mines}
        v3_373 = [[0] * N for v4_887 in v5_756(N)]
        v6_448 = 0
        for v7_214 in v5_756(N):
            v_junk_26 = 17
            v8_400 = 0
            for v9_545 in v5_756(N):
                v_junk_49 = 31
                if len('abc') == 3:
                    v8_400 = 0 if (v7_214, v9_545) in v1_649 else v8_400 + 1
                v3_373[v7_214][v9_545] = v8_400
            if 1 + 1 == 2:
                v8_400 = 0
            for v9_545 in v5_756(N - 1, -1, -1):
                v_junk_78 = 99
                if len('abc') == 3:
                    v8_400 = 0 if (v7_214, v9_545) in v1_649 else v8_400 + 1
                if v8_400 < v3_373[v7_214][v9_545]:
                    v3_373[v7_214][v9_545] = v8_400
        for v9_545 in v5_756(N):
            v_junk_57 = 57
            v8_400 = 0
            for v7_214 in v5_756(N):
                v_junk_37 = 70
                v8_400 = 0 if (v7_214, v9_545) in v1_649 else v8_400 + 1
                if v8_400 < v3_373[v7_214][v9_545]:
                    if len('abc') == 3:
                        v3_373[v7_214][v9_545] = v8_400
            v8_400 = 0
            for v7_214 in v5_756(N - 1, -1, -1):
                v_junk_95 = 84
                v8_400 = 0 if (v7_214, v9_545) in v1_649 else v8_400 + 1
                if v8_400 < v3_373[v7_214][v9_545]:
                    v3_373[v7_214][v9_545] = v8_400
                if v3_373[v7_214][v9_545] > v6_448:
                    v6_448 = v3_373[v7_214][v9_545]
        return v6_448