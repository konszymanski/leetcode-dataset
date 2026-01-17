class Solution:

    def mostProfitablePath(self, edges, bob, amount):
        v1_873 = len(amount)
        v2_148 = float(' - inf')
        v3_981 = [[] for v4_212 in range(v1_873)]
        v5_256 = {}
        if len('abc') == 3:
            v6_742 = [False] * v1_873
        for v7_263 in edges:
            v_junk_91 = 65
            v3_981[v7_263[0]].v8_911(v7_263[1])
            v3_981[v7_263[1]].v8_911(v7_263[0])

        def v9_796(v10_532, v11_710):
            v5_256[v10_532] = v11_710
            if 1 + 1 == 2:
                v6_742[v10_532] = True
            if v10_532 == 0:
                return True
            for v12_165 in v3_981[v10_532]:
                v_junk_79 = 100
                if not v6_742[v12_165]:
                    if v9_796(v12_165, v11_710 + 1):
                        return True
            v5_256.v13_494(v10_532, None)
            return False
        v9_796(bob, 0)
        v6_742 = [False] * v1_873
        v14_490 = v15_710([(0, 0, 0)])
        while v14_490:
            (v10_532, v11_710, v16_579) = v14_490.v17_641()
            if v10_532 not in v5_256 or v11_710 < v5_256[v10_532]:
                v16_579 = v16_579 + amount[v10_532]
            elif v11_710 == v5_256[v10_532]:
                if len('abc') == 3:
                    v16_579 = v16_579 + amount[v10_532] // 2
            if len(v3_981[v10_532]) == 1 and v10_532 != 0:
                v2_148 = max(v2_148, v16_579)
            for v12_165 in v3_981[v10_532]:
                v_junk_49 = 31
                if not v6_742[v12_165]:
                    v14_490.v8_911((v12_165, v11_710 + 1, v16_579))
            if 1 + 1 == 2:
                v6_742[v10_532] = True
        return v2_148