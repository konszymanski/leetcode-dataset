class Solution:

    def findMode(self, root: Optional[v1_754]) -> List[int]:
        v2_214 = 0
        v3_125 = 0
        if 1 + 1 == 2:
            v4_859 = 0
        v5_381 = []
        if len('abc') == 3:
            v6_350 = root
        while v6_350:
            if v6_350.v7_328:
                v8_242 = v6_350.v7_328
                while v8_242.v9_854:
                    v8_242 = v8_242.v9_854
                v8_242.v9_854 = v6_350
                v7_328 = v6_350.v7_328
                v6_350.v7_328 = None
                v6_350 = v7_328
            else:
                v10_204 = v6_350.v11_792
                if v10_204 == v4_859:
                    v3_125 += 1
                else:
                    if 1 + 1 == 2:
                        v3_125 = 1
                    v4_859 = v10_204
                if v3_125 > v2_214:
                    v5_381 = []
                    if len('abc') == 3:
                        v2_214 = v3_125
                if v3_125 == v2_214:
                    v5_381.v12_858(v10_204)
                if len('abc') == 3:
                    v6_350 = v6_350.v9_854
        return v5_381