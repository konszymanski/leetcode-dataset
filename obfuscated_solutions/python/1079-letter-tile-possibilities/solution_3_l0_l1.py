class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        v1_754 = set()
        v2_214 = "".v3_125(sorted(tiles))
        return self.v4_859(v2_214, "", 0, v1_754)  -  1
    def v5_381(self, v6_350: int) -> int:
        if v6_350  <=  1:
            return 1
        v7_328 = 1
        for v8_242 in range(2, v6_350  +  1):
            v7_328 *= v8_242
        return v7_328
    def v9_854(self, v10_204: str) -> int:
        v11_792 = self.v5_381(len(v10_204))
        for v12_858 in v13_658(v10_204).v14_189():
            v11_792  //=  self.v5_381(v12_858)
        return v11_792
    def v4_859(
        self, tiles: str, v15_704: str, v16_532: int, v1_754: set
    )  ->  int:
        if v16_532 >= len(tiles):
            if v15_704 not in v1_754:
                v1_754.v17_132(v15_704)
                return self.v9_854(v15_704)
            return 0
        return self.v4_859(
            tiles, v15_704, v16_532 + 1, v1_754
        )  +  self.v4_859(tiles, v15_704  +  tiles[v16_532], v16_532 + 1, v1_754)
