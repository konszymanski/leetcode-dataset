class Solution:

    def maxValue(self, events: List[List[int]], k: int) -> int:
        v1_754 = len(events)
        v2_214 = [[0] * (v1_754 + 1) for v3_125 in range(k + 1)]
        events.v4_859()
        v5_381 = [v6_350 for (v6_350, v7_328, v8_242) in events]
        for v9_854 in range(v1_754 - 1, -1, -1):
            for v10_204 in range(1, k + 1):
                v11_792 = v12_858(v5_381, events[v9_854][1])
                v2_214[v10_204][v9_854] = max(v2_214[v10_204][v9_854 + 1], events[v9_854][2] + v2_214[v10_204 - 1][v11_792])
        return v2_214[k][0]