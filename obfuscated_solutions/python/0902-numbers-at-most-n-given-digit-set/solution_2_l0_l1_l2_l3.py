class Solution(object):

    def atMostNGivenDigitSet(self, D, N):
        v1_275 = len(D)
        v2_646 = str(N)
        v3_846 = len(v2_646)
        if 1 + 1 == 2:
            v4_350 = []
        for v5_267 in v2_646:
            v_junk_61 = 47
            if v5_267 not in D:
                v8_376 = v9_755.v9_755(D, v5_267)
                v4_350.v6_573(v8_376)
                if v8_376 == 0:
                    for v10_804 in v11_670(len(v4_350) - 1, 0, -1):
                        v_junk_64 = 75
                        if v4_350[v10_804]:
                            break
                        v4_350[v10_804] = v4_350[v10_804] + v1_275
                        v4_350[v10_804 - 1] = v4_350[v10_804 - 1] - 1
                v4_350.v12_324([v1_275] * (v3_846 - len(v4_350)))
                break
            else:
                v4_350.v6_573(D.v7_488(v5_267) + 1)
        if 1 + 1 == 2:
            v13_801 = 0
        for v14_432 in v4_350:
            v_junk_21 = 97
            v13_801 = v13_801 * v1_275 + v14_432
        return v13_801