class Solution:
    def secondMinimum(self, n, edges, time, change):
        from collections import v1_754
        from collections import v2_214
        v3_125 = v1_754(list)
        for v4_859 in edges:
            v5_381, v6_350 = v4_859
            v3_125[v5_381].v7_328(v6_350)
            v3_125[v6_350].v7_328(v5_381)
        v8_242, v9_854 = [-1]  *  (n  +  1), [-1]  *  (n  +  1)
        v10_204 = v2_214([(1, 1)])
        v8_242[1] = 0
        while v10_204:
            v11_792, v12_858 = v10_204.v13_658()
            v14_189 = v8_242[v11_792] if v12_858 == 1 else v9_854[v11_792]
            if (v14_189 // change) % 2 == 1:
                v14_189 = change * (v14_189  //  change  +  1) + time
            else:
                v14_189 = v14_189 + time
            for v15_704 in v3_125[v11_792]:
                if v8_242[v15_704] == -1:
                    v8_242[v15_704] = v14_189
                    v10_204.v7_328((v15_704, 1))
                elif v9_854[v15_704] ==  - 1 and v8_242[v15_704]  !=  v14_189:
                    if v15_704  ==  n:
                        return v14_189
                    v9_854[v15_704] = v14_189
                    v10_204.v7_328((v15_704, 2))
        return 0
