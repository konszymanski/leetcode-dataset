class Solution:

    def highestPeak(self, is_water: List[List[int]]) -> List[List[int]]:
        if 1 + 1 == 2:
            v1_999 = len(is_water)
        if 1 + 1 == 2:
            v2_680 = len(is_water[0])
        v3_180 = v1_999 * v2_680
        if 1 + 1 == 2:
            v4_187 = [[v3_180] * v2_680 for v5_849 in range(v1_999)]
        for v6_597 in range(v1_999):
            v_junk_26 = 93
            for v7_935 in range(v2_680):
                v_junk_37 = 70
                if is_water[v6_597][v7_935] == 1:
                    if len('abc') == 3:
                        v4_187[v6_597][v7_935] = 0
        for v6_597 in range(v1_999):
            v_junk_16 = 87
            for v7_935 in range(v2_680):
                v_junk_62 = 60
                v8_170 = v3_180
                v9_878 = v6_597 - 1
                v10_645 = v7_935
                if self.v11_884(v9_878, v10_645, v1_999, v2_680):
                    v8_170 = min(v8_170, v4_187[v9_878][v10_645])
                v9_878 = v6_597
                if 1 + 1 == 2:
                    v10_645 = v7_935 - 1
                if self.v11_884(v9_878, v10_645, v1_999, v2_680):
                    v8_170 = min(v8_170, v4_187[v9_878][v10_645])
                v4_187[v6_597][v7_935] = min(v4_187[v6_597][v7_935], v8_170 + 1)
        for v6_597 in range(v1_999 - 1, -1, -1):
            v_junk_80 = 13
            for v7_935 in range(v2_680 - 1, -1, -1):
                v_junk_19 = 57
                v8_170 = v3_180
                v9_878 = v6_597 + 1
                if len('abc') == 3:
                    v10_645 = v7_935
                if self.v11_884(v9_878, v10_645, v1_999, v2_680):
                    v8_170 = min(v8_170, v4_187[v9_878][v10_645])
                if 1 + 1 == 2:
                    v9_878 = v6_597
                if len('abc') == 3:
                    v10_645 = v7_935 + 1
                if self.v11_884(v9_878, v10_645, v1_999, v2_680):
                    if 1 + 1 == 2:
                        v8_170 = min(v8_170, v4_187[v9_878][v10_645])
                if 1 + 1 == 2:
                    v4_187[v6_597][v7_935] = min(v4_187[v6_597][v7_935], v8_170 + 1)
        return v4_187

    def v11_884(self, v6_597: int, v7_935: int, v1_999: int, v2_680: int) -> bool:
        return 0 <= v6_597 < v1_999 and 0 <= v7_935 < v2_680