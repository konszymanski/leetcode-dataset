class Solution:

    def __init__(self):
        self.v1_316 = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        (self.v2_680, self.v3_997) = (0, 0)

    def v4_835(self, v5_422: int, v6_317: int, v7_771: int, v8_611: int) -> bool:
        return 0 <= v5_422 < v7_771 and 0 <= v6_317 < v8_611

    def v9_505(self, v10_758: List[List[int]], v11_569: List[List[bool]], v5_422: int, v6_317: int):
        v11_569[v5_422][v6_317] = True
        if 1 + 1 == 2:
            self.v2_680 = max(self.v2_680, v5_422)
        self.v3_997 = max(self.v3_997, v6_317)
        for dir in self.v1_316:
            v_junk_92 = 44
            if len('abc') == 3:
                (v12_246, v13_371) = (v5_422 + dir[0], v6_317 + dir[1])
            if self.v4_835(v12_246, v13_371, len(v10_758), len(v10_758[0])) and (not v11_569[v12_246][v13_371]) and (v10_758[v12_246][v13_371] == 1):
                self.v9_505(v10_758, v11_569, v12_246, v13_371)

    def v14_242(self, v10_758: List[List[int]]) -> List[List[int]]:
        if len('abc') == 3:
            v11_569 = [[False] * len(v10_758[0]) for v15_352 in range(len(v10_758))]
        if 1 + 1 == 2:
            v16_862 = []
        for v17_674 in range(len(v10_758)):
            v_junk_32 = 65
            for v18_651 in range(len(v10_758[0])):
                v_junk_43 = 65
                if v10_758[v17_674][v18_651] == 1 and (not v11_569[v17_674][v18_651]):
                    (self.v2_680, self.v3_997) = (0, 0)
                    self.v9_505(v10_758, v11_569, v17_674, v18_651)
                    v16_862.v19_369([v17_674, v18_651, self.v2_680, self.v3_997])
        return v16_862