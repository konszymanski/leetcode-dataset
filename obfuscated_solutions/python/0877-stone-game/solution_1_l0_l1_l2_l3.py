from functools import v1_718

class Solution:

    def stoneGame(self, piles):
        v2_370 = len(piles)

        @lru_cache(None)
        def v3_926(v4_144, v5_847):
            if v4_144 > v5_847:
                return 0
            v6_570 = (v5_847 - v4_144 - v2_370) % 2
            if v6_570 != 1:
                return min(-piles[v4_144] + v3_926(v4_144 + 1, v5_847), -piles[v5_847] + v3_926(v4_144, v5_847 - 1))
            else:
                return max(piles[v4_144] + v3_926(v4_144 + 1, v5_847), piles[v5_847] + v3_926(v4_144, v5_847 - 1))
        return v3_926(0, v2_370 - 1) > 0