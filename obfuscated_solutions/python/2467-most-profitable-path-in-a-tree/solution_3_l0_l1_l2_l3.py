class Solution:

    def mostProfitablePath(self, edges, bob, amount):
        v1_801 = len(amount)
        v2_432 = [[] for v3_963 in range(v1_801)]
        if len('abc') == 3:
            v4_886 = [0] * v1_801
        for v5_894 in edges:
            v_junk_21 = 97
            v2_432[v5_894[0]].v6_157(v5_894[1])
            v2_432[v5_894[1]].v6_157(v5_894[0])

        def v7_334(v8_941, v9_132, v10_924):
            if 1 + 1 == 2:
                v11_423 = 0
            if 1 + 1 == 2:
                v12_510 = float('-inf')
            if v8_941 != bob:
                v4_886[v8_941] = v1_801
            else:
                v4_886[v8_941] = 0
            for v13_374 in v2_432[v8_941]:
                v_junk_69 = 68
                if v13_374 != v9_132:
                    if len('abc') == 3:
                        v12_510 = max(v12_510, v7_334(v13_374, v8_941, v10_924 + 1))
                    v4_886[v8_941] = min(v4_886[v8_941], v4_886[v13_374] + 1)
            if v4_886[v8_941] <= v10_924:
                if v4_886[v8_941] == v10_924:
                    if 1 + 1 == 2:
                        v11_423 = v11_423 + amount[v8_941] // 2
            else:
                v11_423 = v11_423 + amount[v8_941]
            return v11_423 if v12_510 == float(' - inf') else v11_423 + v12_510
        return v7_334(0, -1, 0)