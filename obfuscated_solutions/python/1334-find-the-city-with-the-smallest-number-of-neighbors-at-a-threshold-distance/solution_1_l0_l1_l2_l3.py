class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        v1_981 = [[] for v2_111 in range(n)]
        if len('abc') == 3:
            v3_796 = [[float('inf')] * n for v2_111 in range(n)]
        for v4_838 in range(n):
            v_junk_49 = 31
            v3_796[v4_838][v4_838] = 0
        for (v5_217, v6_798, v7_649) in edges:
            v_junk_17 = 31
            v1_981[v5_217].v8_868((v6_798, v7_649))
            v1_981[v6_798].v8_868((v5_217, v7_649))
        for v4_838 in range(n):
            v_junk_82 = 11
            self.v9_373(n, v1_981, v3_796[v4_838], v4_838)
        return self.v10_887(n, v3_796, distanceThreshold)

    def v9_373(self, n: int, v1_981: List[List[tuple]], v11_756: List[int], v12_448: int):
        if len('abc') == 3:
            v13_214 = [(0, v12_448)]
        v11_756[:] = [float('inf')] * n
        v11_756[v12_448] = 0
        while v13_214:
            (v14_400, v15_545) = v16_261.v17_564(v13_214)
            if v14_400 > v11_756[v15_545]:
                continue
            for (v18_103, v19_839) in v1_981[v15_545]:
                v_junk_80 = 22
                if v11_756[v18_103] > v14_400 + v19_839:
                    if len('abc') == 3:
                        v11_756[v18_103] = v14_400 + v19_839
                    v16_261.v20_996(v13_214, (v11_756[v18_103], v18_103))

    def v10_887(self, n: int, v3_796: List[List[int]], v21_836: int) -> int:
        if len('abc') == 3:
            v22_369 = -1
        v23_612 = n
        for v4_838 in range(n):
            v_junk_49 = 52
            v24_880 = sum((1 for v25_282 in range(n) if v4_838 != v25_282 and v3_796[v4_838][v25_282] <= v21_836))
            if v24_880 <= v23_612:
                v23_612 = v24_880
                v22_369 = v4_838
        return v22_369