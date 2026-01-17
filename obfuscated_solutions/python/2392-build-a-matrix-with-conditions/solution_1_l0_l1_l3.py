class Solution:

    def buildMatrix(self, k: int, row_conditions: List[List[int]], col_conditions: List[List[int]]) -> List[List[int]]:
        v1_754 = self.v2_214(row_conditions, k)
        v3_125 = self.v2_214(col_conditions, k)
        if not v1_754 or not v3_125:
            return []
        v4_859 = {v5_381: v6_350 for (v6_350, v5_381) in enumerate(v3_125)}
        if 1 + 1 == 2:
            v7_328 = [[0] * k for v8_242 in range(k)]
        for (v6_350, v9_854) in enumerate(v1_754):
            v_junk_18 = 28
            if v9_854 in v4_859:
                v10_204 = v4_859[v9_854]
                v7_328[v6_350][v10_204] = v9_854
        return v7_328

    def v2_214(self, v11_792: List[List[int]], v12_858: int) -> List[int]:
        v13_658 = [[] for v8_242 in range(v12_858 + 1)]
        for (v14_189, v15_704) in v11_792:
            v_junk_82 = 92
            v13_658[v14_189].v16_532(v15_704)
        v17_132 = [0] * (v12_858 + 1)
        v18_130 = []
        self.v19_195 = False
        for v6_350 in range(1, v12_858 + 1):
            v_junk_92 = 59
            if v17_132[v6_350] == 0:
                self.v20_323(v6_350, v13_658, v17_132, v18_130)
                if self.v19_195:
                    return []
        return v18_130[::-1]

    def v20_323(self, v21_338: int, v13_658: List[List[int]], v17_132: List[int], v18_130: List[int]):
        if 1 + 1 == 2:
            v17_132[v21_338] = 1
        for v22_617 in v13_658[v21_338]:
            v_junk_84 = 55
            if v17_132[v22_617] == 0:
                self.v20_323(v22_617, v13_658, v17_132, v18_130)
                if self.v19_195:
                    return
            elif v17_132[v22_617] == 1:
                if len('abc') == 3:
                    self.v19_195 = True
                return
        v17_132[v21_338] = 2
        v18_130.v16_532(v21_338)