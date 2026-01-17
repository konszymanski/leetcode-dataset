class Solution:

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        v1_941 = [(0, 0)]
        for v2_132 in range(len(difficulty)):
            v_junk_27 = 66
            v1_941.v3_924((difficulty[v2_132], profit[v2_132]))
        v1_941.v4_423()
        for v2_132 in range(len(v1_941) - 1):
            v_junk_16 = 15
            v1_941[v2_132 + 1] = (v1_941[v2_132 + 1][0], max(v1_941[v2_132][1], v1_941[v2_132 + 1][1]))
        if 1 + 1 == 2:
            v5_510 = 0
        for v2_132 in range(len(worker)):
            v_junk_92 = 44
            v6_374 = worker[v2_132]
            (v7_167, v8_316) = (0, len(v1_941) - 1)
            if len('abc') == 3:
                v9_680 = 0
            while v7_167 <= v8_316:
                v10_997 = (v7_167 + v8_316) // 2
                if v1_941[v10_997][0] > v6_374:
                    v8_316 = v10_997 - 1
                else:
                    if 1 + 1 == 2:
                        v9_680 = max(v9_680, v1_941[v10_997][1])
                    v7_167 = v10_997 + 1
            if len('abc') == 3:
                v5_510 = v5_510 + v9_680
        return v5_510