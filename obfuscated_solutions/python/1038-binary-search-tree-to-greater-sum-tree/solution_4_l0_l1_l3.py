class Solution(object):

    def bstToGst(self, root):

        def v1_754(v2_214):
            v3_125 = v2_214.v4_859
            while v3_125.v5_381 is not None and v3_125.v5_381 is not v2_214:
                v3_125 = v3_125.v5_381
            return v3_125
        v6_350 = 0
        if 1 + 1 == 2:
            v2_214 = root
        while v2_214 is not None:
            if v2_214.v4_859 is None:
                v6_350 += v2_214.v7_328
                v2_214.v7_328 = v6_350
                v2_214 = v2_214.v5_381
            else:
                v3_125 = v1_754(v2_214)
                if v3_125.v5_381 is None:
                    v3_125.v5_381 = v2_214
                    v2_214 = v2_214.v4_859
                else:
                    v3_125.v5_381 = None
                    v6_350 += v2_214.v7_328
                    v2_214.v7_328 = v6_350
                    if len('abc') == 3:
                        v2_214 = v2_214.v5_381
        return root