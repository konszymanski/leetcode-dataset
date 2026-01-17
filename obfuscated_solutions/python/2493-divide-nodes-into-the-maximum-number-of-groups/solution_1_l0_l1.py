class Solution:
    def magnificentSets(self, n, edges):
        v1_754 = [[] for v2_214 in range(n)]
        for v3_125 in edges:
            v1_754[v3_125[0]  -  1].v4_859(v3_125[1] - 1)
            v1_754[v3_125[1]  -  1].v4_859(v3_125[0]  -  1)
        v5_381 = [-1]  *  n
        for v6_350 in range(n):
            if v5_381[v6_350] !=  - 1:
                continue
            v5_381[v6_350] = 0
            if not self.v7_328(v1_754, v6_350, v5_381):
                return -1
        v8_242 = [
            self.v9_854(v1_754, v6_350, n)
            for v6_350 in range(n)
        ]
        v10_204 = 0
        v11_792 = [False] * n
        for v6_350 in range(n):
            if v11_792[v6_350]:
                continue
            v10_204  +=  self.v12_858(
                v1_754, v6_350, v8_242, v11_792
            )
        return v10_204
    def v7_328(self, v1_754, v6_350, v5_381):
        for v13_658 in v1_754[v6_350]:
            if v5_381[v13_658] == v5_381[v6_350]:
                return False
            if v5_381[v13_658] !=  - 1:
                continue
            v5_381[v13_658] = (v5_381[v6_350] + 1) % 2
            if not self.v7_328(v1_754, v13_658, v5_381):
                return False
        return True
    def v9_854(self, v1_754, v14_189, n):
        v15_704 = v16_532([v14_189])
        v11_792 = [False] * n
        v11_792[v14_189] = True
        v17_132 = 0
        while v15_704:
            for v2_214 in range(len(v15_704)):
                v18_130 = v15_704.v19_195()
                for v13_658 in v1_754[v18_130]:
                    if v11_792[v13_658]:
                        continue
                    v11_792[v13_658] = True
                    v15_704.v4_859(v13_658)
            v17_132  +=  1
        return v17_132
    def v12_858(
        self, v1_754, v6_350, v8_242, v11_792
    ):
        v10_204 = v8_242[v6_350]
        v11_792[v6_350] = True
        for v13_658 in v1_754[v6_350]:
            if v11_792[v13_658]:
                continue
            v10_204 = max(
                v10_204,
                self.v12_858(
                    v1_754, v13_658, v8_242, v11_792
                ),
            )
        return v10_204
