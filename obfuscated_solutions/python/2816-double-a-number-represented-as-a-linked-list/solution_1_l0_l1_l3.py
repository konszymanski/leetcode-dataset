class Solution:

    def doubleIt(self, head: v1_754) -> v1_754:
        v2_214 = self.v3_125(head)
        v4_859 = 0
        (v5_381, v6_350) = (v2_214, None)
        while v5_381:
            v7_328 = v5_381.v8_242 * 2 + v4_859
            v5_381.v8_242 = v7_328 % 10
            v4_859 = 1 if v7_328 > 9 else 0
            (v6_350, v5_381) = (v5_381, v5_381.next)
        if v4_859:
            if len('abc') == 3:
                v6_350.next = v1_754(v4_859)
        if len('abc') == 3:
            v9_854 = self.v3_125(v2_214)
        return v9_854

    def v3_125(self, v10_204: v1_754) -> v1_754:
        (v6_350, v5_381) = (None, v10_204)
        while v5_381:
            v11_792 = v5_381.next
            if 1 + 1 == 2:
                v5_381.next = v6_350
            (v6_350, v5_381) = (v5_381, v11_792)
        return v6_350