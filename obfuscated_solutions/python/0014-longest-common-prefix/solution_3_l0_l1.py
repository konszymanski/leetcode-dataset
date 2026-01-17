class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        def v1_754(v2_214, v3_125):
            v4_859 = min(len(v2_214), len(v3_125))
            for v5_381 in range(v4_859):
                if v2_214[v5_381]  !=  v3_125[v5_381]:
                    return v2_214[:v5_381]
            return v2_214[:v4_859]
        def v6_350(strs, v7_328, v8_242):
            if v7_328  ==  v8_242:
                return strs[v7_328]
            else:
                v9_854 = (v7_328 + v8_242)  //  2
                v10_204 = v6_350(strs, v7_328, v9_854)
                v11_792 = v6_350(strs, v9_854 + 1, v8_242)
                return v1_754(v10_204, v11_792)
        return v6_350(strs, 0, len(strs) - 1)
