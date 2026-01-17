class Solution:
    def findMode(self, root: Optional[v1_754])  ->  List[int]:
        v2_214 = v3_125(int)
        v4_859 = [root]
        while v4_859:
            v5_381 = v4_859.v6_350()
            v2_214[v5_381.v7_328] += 1
            if v5_381.v8_242:
                v4_859.v9_854(v5_381.v8_242)
            if v5_381.v10_204:
                v4_859.v9_854(v5_381.v10_204)
        v11_792 = max(v2_214.v12_858())
        v13_658 = []
        for v14_189 in v2_214:
            if v2_214[v14_189] == v11_792:
                v13_658.v9_854(v14_189)
        return v13_658
