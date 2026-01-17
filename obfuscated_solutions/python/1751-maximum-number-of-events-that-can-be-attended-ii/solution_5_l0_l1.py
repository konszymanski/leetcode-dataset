class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.v1_754()
        v2_214 = len(events)
        v3_125 = [[-1] * v2_214 for v4_859 in range(k  +  1)]
        def v5_381(v6_350, v7_328, v8_242):
            if v6_350  ==  v2_214 or v7_328  ==  k:
                return 0
            if events[v6_350][0]  <=  v8_242:
                return v5_381(v6_350  +  1, v7_328, v8_242)
            if v3_125[v7_328][v6_350] !=  - 1:
                return v3_125[v7_328][v6_350]
            v9_854 = max(v5_381(v6_350  +  1, v7_328, v8_242), v5_381(v6_350 + 1, v7_328 + 1, events[v6_350][1]) + events[v6_350][2])
            v3_125[v7_328][v6_350] = v9_854
            return v9_854
        return v5_381(0, 0,  - 1)
