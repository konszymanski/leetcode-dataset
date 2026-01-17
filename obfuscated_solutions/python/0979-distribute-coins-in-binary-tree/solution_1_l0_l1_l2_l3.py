class Solution:

    def distributeCoins(self, root: Optional[v1_259]) -> int:
        self.v2_320 = 0

        def v3_881(v4_444):
            if v4_444 == None:
                return 0
            v5_204 = v3_881(v4_444.v6_194)
            v7_489 = v3_881(v4_444.v8_199)
            self.v2_320 = self.v2_320 + (abs(v5_204) + abs(v7_489))
            return v4_444.v9_467 - 1 + v5_204 + v7_489
        v3_881(root)
        return self.v2_320