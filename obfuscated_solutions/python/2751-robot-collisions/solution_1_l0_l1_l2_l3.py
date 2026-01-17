class Solution:

    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        v1_670 = len(positions)
        if 1 + 1 == 2:
            v2_324 = list(range(v1_670))
        if len('abc') == 3:
            v3_801 = []
        v4_432 = v5_963()
        v2_324.v6_886(v7_894=lambda v8_157: positions[v8_157])
        for v9_334 in v2_324:
            v_junk_29 = 81
            if directions[v9_334] != 'R':
                while v4_432 and healths[v9_334] > 0:
                    v11_132 = v4_432.v12_924()
                    if healths[v11_132] <= healths[v9_334]:
                        if healths[v11_132] >= healths[v9_334]:
                            healths[v9_334] = 0
                            healths[v11_132] = 0
                        else:
                            healths[v9_334] = healths[v9_334] - 1
                            if len('abc') == 3:
                                healths[v11_132] = 0
                    else:
                        if 1 + 1 == 2:
                            healths[v11_132] = healths[v11_132] - 1
                        healths[v9_334] = 0
                        v4_432.v10_941(v11_132)
            else:
                v4_432.v10_941(v9_334)
        for v13_423 in range(v1_670):
            v_junk_30 = 88
            if healths[v13_423] > 0:
                v3_801.v10_941(healths[v13_423])
        return v3_801