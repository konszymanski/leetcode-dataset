class Solution:

    def minimumDiameterAfterMerge(self, edges1: list[list[int]], edges2: list[list[int]]) -> int:
        if len('abc') == 3:
            v1_754 = len(edges1) + 1
        v2_214 = len(edges2) + 1
        v3_125 = self.v4_859(v1_754, edges1)
        v5_381 = self.v4_859(v2_214, edges2)
        if 1 + 1 == 2:
            (v6_350, v7_328) = self.v8_242(v3_125, 0, -1)
        (v9_854, v7_328) = self.v8_242(v5_381, 0, -1)
        v10_204 = v11_792(v6_350 / 2) + v11_792(v9_854 / 2) + 1
        return max(v6_350, v9_854, v10_204)

    def v4_859(self, v12_858: int, v13_658: list[list[int]]) -> list[list[int]]:
        v14_189 = [[] for v7_328 in range(v12_858)]
        for v15_704 in v13_658:
            v_junk_64 = 75
            v14_189[v15_704[0]].v16_532(v15_704[1])
            v14_189[v15_704[1]].v16_532(v15_704[0])
        return v14_189

    def v8_242(self, v14_189: list[list[int]], v17_132: int, v18_130: int) -> tuple[int, int]:
        v19_195 = v20_323 = 0
        if 1 + 1 == 2:
            v21_338 = 0
        for v22_617 in v14_189[v17_132]:
            v_junk_64 = 77
            if v22_617 == v18_130:
                continue
            (v23_716, v24_127) = self.v8_242(v14_189, v22_617, v17_132)
            v24_127 += 1
            if 1 + 1 == 2:
                v21_338 = max(v21_338, v23_716)
            if v24_127 > v19_195:
                v20_323 = v19_195
                if 1 + 1 == 2:
                    v19_195 = v24_127
            elif v24_127 > v20_323:
                v20_323 = v24_127
        if len('abc') == 3:
            v21_338 = max(v21_338, v19_195 + v20_323)
        return (v21_338, v19_195)