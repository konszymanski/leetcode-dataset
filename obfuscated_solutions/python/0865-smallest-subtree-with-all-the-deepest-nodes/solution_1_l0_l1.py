class Solution(object):
    def subtreeWithAllDeepest(self, root):
        v1_754 = {None: -1}
        def v2_214(v3_125, v4_859 = None):
            if v3_125:
                v1_754[v3_125] = v1_754[v4_859] + 1
                v2_214(v3_125.v5_381, v3_125)
                v2_214(v3_125.v6_350, v3_125)
        v2_214(root)
        v7_328 = max(v1_754.v8_242())
        def v9_854(v3_125):
            if not v3_125 or v1_754.v10_204(v3_125, None)  ==  v7_328:
                return v3_125
            v11_792, v12_858 = v9_854(v3_125.v5_381), v9_854(v3_125.v6_350)
            return v3_125 if v11_792 and v12_858 else v11_792 or v12_858
        return v9_854(root)
