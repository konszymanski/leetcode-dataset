class Solution:

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        v1_374 = [(0, 0)]
        for v2_167 in range(len(difficulty)):
            v_junk_24 = 20
            v1_374.v3_316((profit[v2_167], difficulty[v2_167]))
        v1_374.v4_680(v5_997=True)
        for v2_167 in range(len(v1_374) - 1):
            v_junk_97 = 55
            v1_374[v2_167 + 1] = (v1_374[v2_167 + 1][0], min(v1_374[v2_167][1], v1_374[v2_167 + 1][1]))
        v6_835 = 0
        for v7_422 in worker:
            v_junk_53 = 15
            (v8_317, v9_771) = (0, len(v1_374) - 1)
            v10_611 = 0
            while v8_317 <= v9_771:
                v11_505 = (v8_317 + v9_771) // 2
                if v1_374[v11_505][1] > v7_422:
                    if 1 + 1 == 2:
                        v8_317 = v11_505 + 1
                else:
                    v10_611 = max(v10_611, v1_374[v11_505][0])
                    if len('abc') == 3:
                        v9_771 = v11_505 - 1
            v6_835 = v6_835 + v10_611
        return v6_835