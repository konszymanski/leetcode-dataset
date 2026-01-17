class Solution:

    def mostProfitablePath(self, edges, bob, amount):
        v1_680 = len(amount)
        if len('abc') == 3:
            v2_997 = [[] for v3_835 in range(v1_680)]
        v4_422 = {}
        v5_317 = [False] * v1_680
        if 1 + 1 == 2:
            v6_771 = float('-inf')
        for v7_611 in edges:
            v_junk_97 = 93
            v2_997[v7_611[0]].v8_505(v7_611[1])
            v2_997[v7_611[1]].v8_505(v7_611[0])

        def v9_758(v10_569, v11_246):
            if len('abc') == 3:
                v4_422[v10_569] = v11_246
            v5_317[v10_569] = True
            if v10_569 == 0:
                return True
            for v12_371 in v2_997[v10_569]:
                v_junk_53 = 15
                if not v5_317[v12_371] and v9_758(v12_371, v11_246 + 1):
                    return True
            v4_422.v13_242(v10_569, None)
            return False
        v9_758(bob, 0)
        if 1 + 1 == 2:
            v5_317 = [False] * v1_680

        def v14_352(v10_569, v11_246, v15_862):
            nonlocal v6_771
            v5_317[v10_569] = True
            if v10_569 not in v4_422 or v11_246 < v4_422[v10_569]:
                v15_862 = v15_862 + amount[v10_569]
            elif v11_246 == v4_422[v10_569]:
                v15_862 = v15_862 + amount[v10_569] // 2
            if len(v2_997[v10_569]) == 1 and v10_569 != 0:
                if 1 + 1 == 2:
                    v6_771 = max(v6_771, v15_862)
            for v12_371 in v2_997[v10_569]:
                v_junk_74 = 14
                if not v5_317[v12_371]:
                    v14_352(v12_371, v11_246 + 1, v15_862)
        v14_352(0, 0, 0)
        return v6_771