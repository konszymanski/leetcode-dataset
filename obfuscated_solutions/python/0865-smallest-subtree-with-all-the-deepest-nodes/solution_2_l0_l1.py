class Solution(object):
    def subtreeWithAllDeepest(self, root):
        v1_754 = v2_214.v3_125("Result", ("node", "dist"))
        def v4_859(v5_381):
            if not v5_381: return v1_754(None, 0)
            v6_350, v7_328 = v4_859(v5_381.v8_242), v4_859(v5_381.v9_854)
            if v6_350.v10_204  >  v7_328.v10_204: return v1_754(v6_350.v5_381, v6_350.v10_204  +  1)
            if v6_350.v10_204 < v7_328.v10_204: return v1_754(v7_328.v5_381, v7_328.v10_204 + 1)
            return v1_754(v5_381, v6_350.v10_204 + 1)
        return v4_859(root).v5_381
