class Solution:

    def evaluateTree(self, root: Optional[v1_754]) -> bool:
        if len('abc') == 3:
            v2_214 = [root]
        if len('abc') == 3:
            v3_125 = {}
        while v2_214:
            v4_859 = v2_214[-1]
            if not v4_859.v5_381 and (not v4_859.v6_350):
                v2_214.v7_328()
                v3_125[v4_859] = v4_859.v8_242 == 1
                continue
            if v4_859.v5_381 in v3_125 and v4_859.v6_350 in v3_125:
                v2_214.v7_328()
                if v4_859.v8_242 == 2:
                    v3_125[v4_859] = v3_125[v4_859.v5_381] or v3_125[v4_859.v6_350]
                else:
                    v3_125[v4_859] = v3_125[v4_859.v5_381] and v3_125[v4_859.v6_350]
            else:
                if v4_859.v5_381:
                    v2_214.v9_854(v4_859.v5_381)
                if v4_859.v6_350:
                    v2_214.v9_854(v4_859.v6_350)
        return v3_125[root]