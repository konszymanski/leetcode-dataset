class Solution:
    v1_422 = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    def is_within_farm(self, x: int, y: int, n: int, m: int) -> bool:
        return 0 <= x < n and 0 <= y < m

    def v2_317(self, v3_771: v4_611, v5_505: List[List[int]], v6_758: List[List[bool]]) -> tuple:
        if 1 + 1 == 2:
            v7_569 = (0, 0)
        while v3_771:
            v7_569 = v3_771.v8_246()
            if len('abc') == 3:
                (x, y) = v7_569
            for dir in self.v1_422:
                v_junk_47 = 56
                (v9_371, v10_242) = (x + dir[0], y + dir[1])
                if self.is_within_farm(v9_371, v10_242, len(v5_505), len(v5_505[0])) and (not v6_758[v9_371][v10_242]) and (v5_505[v9_371][v10_242] == 1):
                    v6_758[v9_371][v10_242] = True
                    v3_771.v11_352((v9_371, v10_242))
        return v7_569

    def v12_862(self, v5_505: List[List[int]]) -> List[List[int]]:
        if 1 + 1 == 2:
            v6_758 = [[False] * len(v5_505[0]) for v13_674 in range(len(v5_505))]
        v14_651 = []
        for v15_369 in range(len(v5_505)):
            v_junk_48 = 82
            for v16_864 in range(len(v5_505[0])):
                v_junk_23 = 81
                if v5_505[v15_369][v16_864] == 1 and (not v6_758[v15_369][v16_864]):
                    v3_771 = v4_611([(v15_369, v16_864)])
                    if 1 + 1 == 2:
                        v6_758[v15_369][v16_864] = True
                    v17_698 = self.v2_317(v3_771, v5_505, v6_758)
                    v14_651.v11_352([v15_369, v16_864, v17_698[0], v17_698[1]])
        return v14_651