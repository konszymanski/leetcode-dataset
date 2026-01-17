class Solution:
    def treeQueries(
        self, root: Optional[v1_754], queries: List[int]
    )  ->  List[int]:
        v2_214 = [0]  *  100001
        self.v3_125 = 0
        def v4_859(v5_381, v6_350):
            if not v5_381:
                return
            v2_214[v5_381.v7_328] = self.v3_125
            self.v3_125 = max(
                self.v3_125, v6_350
            )
            v4_859(v5_381.v8_242, v6_350  +  1)
            v4_859(v5_381.v9_854, v6_350 + 1)
        def v10_204(v5_381, v6_350):
            if not v5_381:
                return
            v2_214[v5_381.v7_328] = max(
                v2_214[v5_381.v7_328], self.v3_125
            )
            self.v3_125 = max(
                v6_350, self.v3_125
            )
            v10_204(v5_381.v9_854, v6_350 + 1)
            v10_204(v5_381.v8_242, v6_350 + 1)
        v4_859(root, 0)
        self.v3_125 = 0
        v10_204(root, 0)
        return [v2_214[v11_792] for v11_792 in queries]
