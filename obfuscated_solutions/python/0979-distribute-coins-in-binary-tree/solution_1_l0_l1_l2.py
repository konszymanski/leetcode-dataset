class Solution:

    def distributeCoins(self, root: Optional[v1_754]) -> int:
        self.v2_214 = 0

        def v3_125(v4_859):
            if v4_859 == None:
                return 0
            v5_381 = v3_125(v4_859.v6_350)
            v7_328 = v3_125(v4_859.v8_242)
            self.v2_214 = self.v2_214 + (abs(v5_381) + abs(v7_328))
            return v4_859.v9_854 - 1 + v5_381 + v7_328
        v3_125(root)
        return self.v2_214