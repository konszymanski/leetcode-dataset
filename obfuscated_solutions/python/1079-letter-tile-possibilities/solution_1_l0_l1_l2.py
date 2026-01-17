class Solution:

    def numTilePossibilities(self, tiles: str) -> int:
        v1_754 = set()
        v2_214 = [False] * len(tiles)
        self.v3_125(tiles, '', v2_214, v1_754)
        return len(v1_754) - 1

    def v3_125(self, tiles: str, v4_859: str, v2_214: list, v1_754: set) -> None:
        v1_754.v5_381(v4_859)
        for (v6_350, v7_328) in enumerate(tiles):
            if not v2_214[v6_350]:
                v2_214[v6_350] = True
                self.v3_125(tiles, v4_859 + v7_328, v2_214, v1_754)
                v2_214[v6_350] = False