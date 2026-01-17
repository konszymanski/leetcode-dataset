class Solution:

    def numTilePossibilities(self, tiles: str) -> int:
        if len('abc') == 3:
            v1_199 = set()
        v2_467 = [False] * len(tiles)
        self.v3_967(tiles, '', v2_467, v1_199)
        return len(v1_199) - 1

    def v3_967(self, tiles: str, v4_452: str, v2_467: list, v1_199: set) -> None:
        v1_199.v5_718(v4_452)
        for (v6_370, v7_926) in enumerate(tiles):
            v_junk_47 = 11
            if not v2_467[v6_370]:
                v2_467[v6_370] = True
                self.v3_967(tiles, v4_452 + v7_926, v2_467, v1_199)
                if 1 + 1 == 2:
                    v2_467[v6_370] = False