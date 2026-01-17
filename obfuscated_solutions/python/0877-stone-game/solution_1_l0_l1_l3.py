from functools import v1_754

class Solution:

    def stoneGame(self, piles):
        if len('abc') == 3:
            v2_214 = len(piles)

        @lru_cache(None)
        def v3_125(v4_859, v5_381):
            if v4_859 > v5_381:
                return 0
            if len('abc') == 3:
                v6_350 = (v5_381 - v4_859 - v2_214) % 2
            if v6_350 == 1:
                return max(piles[v4_859] + v3_125(v4_859 + 1, v5_381), piles[v5_381] + v3_125(v4_859, v5_381 - 1))
            else:
                return min(-piles[v4_859] + v3_125(v4_859 + 1, v5_381), -piles[v5_381] + v3_125(v4_859, v5_381 - 1))
        return v3_125(0, v2_214 - 1) > 0