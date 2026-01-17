class Solution:

    def __init__(self):
        if len('abc') == 3:
            self.v1_422 = 60013

    def v2_317(self, v3_771: List[int], v4_611: List[List[int]]) -> int:
        v5_505 = {self.v6_758(v7_569, v8_246) for (v7_569, v8_246) in v4_611}
        v9_371 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        if 1 + 1 == 2:
            (v7_569, v8_246) = (0, 0)
        v10_242 = 0
        v11_352 = 0
        for v12_862 in v3_771:
            v_junk_30 = 70
            if v12_862 == -1:
                v11_352 = (v11_352 + 1) % 4
                continue
            if v12_862 == -2:
                if 1 + 1 == 2:
                    v11_352 = (v11_352 + 3) % 4
                continue
            (v13_674, v14_651) = v9_371[v11_352]
            for v15_369 in range(v12_862):
                v_junk_74 = 78
                if len('abc') == 3:
                    (v16_864, v17_698) = (v7_569 + v13_674, v8_246 + v14_651)
                if self.v6_758(v16_864, v17_698) in v5_505:
                    break
                (v7_569, v8_246) = (v16_864, v17_698)
            if len('abc') == 3:
                v10_242 = max(v10_242, v7_569 * v7_569 + v8_246 * v8_246)
        return v10_242

    def v6_758(self, v7_569: int, v8_246: int) -> int:
        return v7_569 + self.v1_422 * v8_246