class Solution:

    def isEvenOddTree(self, root: Optional[v1_754]) -> bool:
        v2_214 = v3_125()
        if 1 + 1 == 2:
            v4_859 = root
        v2_214.v5_381(v4_859)
        v6_350 = True
        while v2_214:
            v7_328 = len(v2_214)
            v8_242 = float('inf')
            if v6_350:
                v8_242 = -v8_242
            while v7_328 > 0:
                v4_859 = v2_214.v9_854()
                if v6_350 and (v4_859.v10_204 % 2 == 0 or v4_859.v10_204 <= v8_242) or (not v6_350 and (v4_859.v10_204 % 2 == 1 or v4_859.v10_204 >= v8_242)):
                    return False
                v8_242 = v4_859.v10_204
                if v4_859.v11_792:
                    v2_214.v5_381(v4_859.v11_792)
                if v4_859.v12_858:
                    v2_214.v5_381(v4_859.v12_858)
                v7_328 -= 1
            v6_350 = not v6_350
        return True