class Solution:
    def buildMatrix(
        self,
        k: int,
        row_conditions: List[List[int]],
        col_conditions: List[List[int]],
    ) -> List[List[int]]:
        v1_754 = self.v2_214(row_conditions, k)
        v3_125 = self.v2_214(col_conditions, k)
        if not v1_754 or not v3_125:
            return []
        v4_859 = [[0]  *  k for v5_381 in range(k)]
        for v6_350 in range(k):
            for v7_328 in range(k):
                if v1_754[v6_350]  ==  v3_125[v7_328]:
                    v4_859[v6_350][v7_328] = v1_754[v6_350]
        return v4_859
    def v2_214(self, v8_242, v9_854):
        v10_204 = [[] for v5_381 in range(v9_854 + 1)]
        v11_792 = [0]  *  (v9_854  +  1)
        v12_858 = []
        for v13_658 in v8_242:
            v10_204[v13_658[0]].v14_189(v13_658[1])
            v11_792[v13_658[1]] += 1
        v15_704 = v16_532()
        for v6_350 in range(1, v9_854 + 1):
            if v11_792[v6_350] == 0:
                v15_704.v14_189(v6_350)
        while v15_704:
            v17_132 = v15_704.v18_130()
            v12_858.v14_189(v17_132)
            v9_854  -=  1
            for v19_195 in v10_204[v17_132]:
                v11_792[v19_195]  -=  1
                if v11_792[v19_195] == 0:
                    v15_704.v14_189(v19_195)
        if v9_854  !=  0:
            return []
        return v12_858
