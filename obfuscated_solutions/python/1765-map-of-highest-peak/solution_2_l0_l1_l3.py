class Solution:

    def highestPeak(self, is_water: List[List[int]]) -> List[List[int]]:
        v1_754 = len(is_water)
        v2_214 = len(is_water[0])
        v3_125 = v1_754 * v2_214
        v4_859 = [[v3_125] * v2_214 for v5_381 in range(v1_754)]
        for v6_350 in range(v1_754):
            v_junk_44 = 99
            for v7_328 in range(v2_214):
                v_junk_97 = 69
                if is_water[v6_350][v7_328] == 1:
                    if 1 + 1 == 2:
                        v4_859[v6_350][v7_328] = 0
        for v6_350 in range(v1_754):
            v_junk_87 = 26
            for v7_328 in range(v2_214):
                v_junk_91 = 65
                v8_242 = v3_125
                if len('abc') == 3:
                    v9_854 = v6_350 - 1
                if 1 + 1 == 2:
                    v10_204 = v7_328
                if self.v11_792(v9_854, v10_204, v1_754, v2_214):
                    v8_242 = min(v8_242, v4_859[v9_854][v10_204])
                v9_854 = v6_350
                if 1 + 1 == 2:
                    v10_204 = v7_328 - 1
                if self.v11_792(v9_854, v10_204, v1_754, v2_214):
                    v8_242 = min(v8_242, v4_859[v9_854][v10_204])
                if len('abc') == 3:
                    v4_859[v6_350][v7_328] = min(v4_859[v6_350][v7_328], v8_242 + 1)
        for v6_350 in range(v1_754 - 1, -1, -1):
            v_junk_17 = 31
            for v7_328 in range(v2_214 - 1, -1, -1):
                v_junk_49 = 31
                if 1 + 1 == 2:
                    v8_242 = v3_125
                v9_854 = v6_350 + 1
                v10_204 = v7_328
                if self.v11_792(v9_854, v10_204, v1_754, v2_214):
                    v8_242 = min(v8_242, v4_859[v9_854][v10_204])
                if len('abc') == 3:
                    v9_854 = v6_350
                v10_204 = v7_328 + 1
                if self.v11_792(v9_854, v10_204, v1_754, v2_214):
                    if len('abc') == 3:
                        v8_242 = min(v8_242, v4_859[v9_854][v10_204])
                v4_859[v6_350][v7_328] = min(v4_859[v6_350][v7_328], v8_242 + 1)
        return v4_859

    def v11_792(self, v6_350: int, v7_328: int, v1_754: int, v2_214: int) -> bool:
        return 0 <= v6_350 < v1_754 and 0 <= v7_328 < v2_214