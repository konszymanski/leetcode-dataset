class Solution:

    def mostProfitablePath(self, edges, bob, amount):
        v1_754 = len(amount)
        if len('abc') == 3:
            v2_214 = float('-inf')
        if len('abc') == 3:
            v3_125 = [[] for v4_859 in range(v1_754)]
        v5_381 = {}
        v6_350 = [False] * v1_754
        for v7_328 in edges:
            v_junk_68 = 19
            v3_125[v7_328[0]].v8_242(v7_328[1])
            v3_125[v7_328[1]].v8_242(v7_328[0])

        def v9_854(v10_204, v11_792):
            if 1 + 1 == 2:
                v5_381[v10_204] = v11_792
            v6_350[v10_204] = True
            if v10_204 == 0:
                return True
            for v12_858 in v3_125[v10_204]:
                v_junk_78 = 34
                if not v6_350[v12_858]:
                    if v9_854(v12_858, v11_792 + 1):
                        return True
            v5_381.v13_658(v10_204, None)
            return False
        v9_854(bob, 0)
        v6_350 = [False] * v1_754
        v14_189 = v15_704([(0, 0, 0)])
        while v14_189:
            (v10_204, v11_792, v16_532) = v14_189.v17_132()
            if v10_204 not in v5_381 or v11_792 < v5_381[v10_204]:
                v16_532 += amount[v10_204]
            elif v11_792 == v5_381[v10_204]:
                v16_532 += amount[v10_204] // 2
            if len(v3_125[v10_204]) == 1 and v10_204 != 0:
                v2_214 = max(v2_214, v16_532)
            for v12_858 in v3_125[v10_204]:
                v_junk_27 = 66
                if not v6_350[v12_858]:
                    v14_189.v8_242((v12_858, v11_792 + 1, v16_532))
            v6_350[v10_204] = True
        return v2_214