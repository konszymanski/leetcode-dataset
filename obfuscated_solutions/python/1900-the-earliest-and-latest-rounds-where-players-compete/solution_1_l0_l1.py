class Solution:
    def earliestAndLatest(
        self, n: int, firstPlayer: int, secondPlayer: int
    ) -> List[int]:
        @cache
        def v1_754(n: int, v2_214: int, v3_125: int) -> (int, int):
            if v2_214 + v3_125 == n  +  1:
                return (1, 1)
            if v2_214  +  v3_125 > n  +  1:
                return v1_754(n, n  +  1 - v3_125, n  +  1  -  v2_214)
            v4_859, v5_381 = float("inf"), float("-inf")
            v6_350 = (n + 1) // 2
            if v3_125  <=  v6_350:
                for v7_328 in range(v2_214):
                    for v8_242 in range(v3_125  -  v2_214):
                        v9_854, v10_204 = v1_754(v6_350, v7_328 + 1, v7_328 + v8_242 + 2)
                        v4_859 = min(v4_859, v9_854)
                        v5_381 = max(v5_381, v10_204)
            else:
                v11_792 = n  +  1  -  v3_125
                v12_858 = (n  -  2  *  v11_792  +  1) // 2
                for v7_328 in range(v2_214):
                    for v8_242 in range(v11_792  -  v2_214):
                        v9_854, v10_204 = v1_754(v6_350, v7_328 + 1, v7_328  +  v8_242  +  v12_858  +  2)
                        v4_859 = min(v4_859, v9_854)
                        v5_381 = max(v5_381, v10_204)
            return (v4_859  +  1, v5_381  +  1)
        if firstPlayer  >  secondPlayer:
            firstPlayer, secondPlayer = secondPlayer, firstPlayer
        v4_859, v5_381 = v1_754(n, firstPlayer, secondPlayer)
        v1_754.v13_658()
        return [v4_859, v5_381]
