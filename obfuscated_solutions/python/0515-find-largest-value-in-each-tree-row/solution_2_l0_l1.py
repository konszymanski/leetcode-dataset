class Solution:
    def largestValues(self, root: Optional[v1_754]) -> List[int]:
        def v2_214(v3_125, v4_859):
            if not v3_125:
                return
            if v4_859  ==  len(v5_381):
                v5_381.v6_350(v3_125.v7_328)
            else:
                v5_381[v4_859] = max(v5_381[v4_859], v3_125.v7_328)
            v2_214(v3_125.v8_242, v4_859  +  1)
            v2_214(v3_125.v9_854, v4_859  +  1)
        v5_381 = []
        v2_214(root, 0)
        return v5_381
