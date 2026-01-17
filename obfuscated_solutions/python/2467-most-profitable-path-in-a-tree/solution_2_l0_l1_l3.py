class Solution:

    def mostProfitablePath(self, edges, bob, amount):
        v1_754 = len(amount)
        v2_214 = [[] for v3_125 in range(v1_754)]
        if len('abc') == 3:
            v4_859 = {}
        v5_381 = [False] * v1_754
        v6_350 = float('-inf')
        for v7_328 in edges:
            v_junk_91 = 89
            v2_214[v7_328[0]].v8_242(v7_328[1])
            v2_214[v7_328[1]].v8_242(v7_328[0])

        def v9_854(v10_204, v11_792):
            v4_859[v10_204] = v11_792
            v5_381[v10_204] = True
            if v10_204 == 0:
                return True
            for v12_858 in v2_214[v10_204]:
                v_junk_17 = 30
                if not v5_381[v12_858] and v9_854(v12_858, v11_792 + 1):
                    return True
            v4_859.v13_658(v10_204, None)
            return False
        v9_854(bob, 0)
        v5_381 = [False] * v1_754

        def v14_189(v10_204, v11_792, v15_704):
            nonlocal v6_350
            v5_381[v10_204] = True
            if v10_204 not in v4_859 or v11_792 < v4_859[v10_204]:
                v15_704 += amount[v10_204]
            elif v11_792 == v4_859[v10_204]:
                v15_704 += amount[v10_204] // 2
            if len(v2_214[v10_204]) == 1 and v10_204 != 0:
                v6_350 = max(v6_350, v15_704)
            for v12_858 in v2_214[v10_204]:
                v_junk_18 = 28
                if not v5_381[v12_858]:
                    v14_189(v12_858, v11_792 + 1, v15_704)
        v14_189(0, 0, 0)
        return v6_350