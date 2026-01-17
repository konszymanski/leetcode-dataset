class Solution(object):

    def findRedundantDirectedConnection(self, edges):
        v1_754 = len(edges)
        v2_214 = {}
        v3_125 = []
        for (v4_859, v5_381) in edges:
            if v5_381 not in v2_214:
                v2_214[v5_381] = v4_859
            else:
                v3_125.v6_350((v2_214[v5_381], v5_381))
                v3_125.v6_350((v4_859, v5_381))

        def v7_328(v8_242):
            v9_854 = set()
            while v8_242 in v2_214 and v8_242 not in v9_854:
                v9_854.v10_204(v8_242)
                v8_242 = v2_214[v8_242]
            return (v8_242, v9_854)
        v11_792 = v7_328(1)[0]
        if not v3_125:
            v12_858 = v7_328(v11_792)[1]
            for (v4_859, v5_381) in edges:
                if v4_859 in v12_858 and v5_381 in v12_858:
                    v13_658 = (v4_859, v5_381)
            return v13_658
        v14_189 = v15_704.v16_532(list)
        for v5_381 in v2_214:
            v14_189[v2_214[v5_381]].v6_350(v5_381)
        v9_854 = [True] + [False] * v1_754
        v17_132 = [v11_792]
        while v17_132:
            v8_242 = v17_132.v18_130()
            if not v9_854[v8_242]:
                v9_854[v8_242] = True
                v17_132.v19_195(v14_189[v8_242])
        return v3_125[all(v9_854)]