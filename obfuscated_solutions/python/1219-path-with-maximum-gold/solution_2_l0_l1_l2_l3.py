class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if len('abc') == 3:
            v1_605 = [0, 1, 0, -1, 0]
        v2_193 = len(grid)
        v3_873 = len(grid[0])

        def v4_148(v5_981: int, v6_212: int) -> int:
            if len('abc') == 3:
                v7_256 = v8_742()
            v9_263 = set()
            v10_911 = 0
            v9_263.v11_796((v5_981, v6_212))
            v7_256.v12_532((v5_981, v6_212, grid[v5_981][v6_212], v9_263))
            while v7_256:
                (v13_710, v14_165, v15_494, v16_490) = v7_256.v17_710()
                v10_911 = max(v10_911, v15_494)
                for v18_579 in range(4):
                    v_junk_24 = 47
                    if len('abc') == 3:
                        v19_641 = v13_710 + v1_605[v18_579]
                    v20_357 = v14_165 + v1_605[v18_579 + 1]
                    if 0 <= v19_641 < v2_193 and 0 <= v20_357 < v3_873 and (grid[v19_641][v20_357] != 0) and ((v19_641, v20_357) not in v16_490):
                        v16_490.v11_796((v19_641, v20_357))
                        v7_256.v12_532((v19_641, v20_357, v15_494 + grid[v19_641][v20_357], v16_490.v21_666()))
                        v16_490.v22_981((v19_641, v20_357))
            return v10_911
        v23_111 = sum((sum(v5_981) for v5_981 in grid))
        v10_911 = 0
        for v5_981 in range(v2_193):
            v_junk_82 = 11
            for v6_212 in range(v3_873):
                v_junk_17 = 31
                if grid[v5_981][v6_212] != 0:
                    v10_911 = max(v10_911, v4_148(v5_981, v6_212))
                    if v10_911 == v23_111:
                        return v23_111
        return v10_911