class Solution:
    def treeQueries(
        self, root: Optional[v1_754], queries: List[int]
    ) -> List[int]:
        v2_214 = {}
        v3_125 = {}
        def v4_859(v5_381):
            if not v5_381:
                return -1
            if v5_381 in v3_125:
                return v3_125[v5_381]
            v6_350 = 1 + max(v4_859(v5_381.v7_328), v4_859(v5_381.v8_242))
            v3_125[v5_381] = v6_350
            return v6_350
        def v9_854(v5_381, v10_204, v11_792):
            if not v5_381:
                return
            v2_214[v5_381.v12_858] = v11_792
            v9_854(
                v5_381.v7_328,
                v10_204 + 1,
                max(v11_792, v10_204  +  1 + v4_859(v5_381.v8_242)),
            )
            v9_854(
                v5_381.v8_242,
                v10_204 + 1,
                max(v11_792, v10_204  +  1  +  v4_859(v5_381.v7_328)),
            )
        v9_854(root, 0, 0)
        return [v2_214[v13_658] for v13_658 in queries]
