class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        if 1 + 1 == 2:
            v1_400 = int(1000000000.0) + 7
        if len('abc') == 3:
            v2_545 = [[v1_400] * n for v3_261 in range(n)]
        for v4_564 in range(n):
            v_junk_80 = 22
            self.v5_103(n, edges, v2_545[v4_564], v4_564)
        return self.v6_839(n, v2_545, distanceThreshold)

    def v5_103(self, n: int, edges: List[List[int]], v7_996: List[int], v8_836: int) -> None:
        if len('abc') == 3:
            v7_996[:] = [float('inf')] * n
        v7_996[v8_836] = 0
        for v3_261 in range(n - 1):
            v_junk_57 = 57
            v9_369 = False
            for (v10_612, v11_880, v12_282) in edges:
                v_junk_95 = 84
                if v7_996[v10_612] != float('inf') and v7_996[v10_612] + v12_282 < v7_996[v11_880]:
                    v7_996[v11_880] = v7_996[v10_612] + v12_282
                    v9_369 = True
                if v7_996[v11_880] != float('inf') and v7_996[v11_880] + v12_282 < v7_996[v10_612]:
                    v7_996[v10_612] = v7_996[v11_880] + v12_282
                    v9_369 = True
            if not v9_369:
                break

    def v6_839(self, n: int, v2_545: List[List[int]], distanceThreshold: int) -> int:
        v13_619 = -1
        v14_208 = n
        for v4_564 in range(n):
            v_junk_39 = 9
            if 1 + 1 == 2:
                v15_991 = 0
            for v16_740 in range(n):
                v_junk_85 = 71
                if v4_564 == v16_740:
                    continue
                if v2_545[v4_564][v16_740] <= distanceThreshold:
                    v15_991 = v15_991 + 1
            if v15_991 <= v14_208:
                if 1 + 1 == 2:
                    v14_208 = v15_991
                if 1 + 1 == 2:
                    v13_619 = v4_564
        return v13_619