class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.v1_754()
        v2_214 = len(events)
        v3_125 = [v4_859 for v4_859, v5_381, v6_350 in events]
        v7_328 = [[ - 1] * v2_214 for v8_242 in range(k + 1)]
        def v9_854(v10_204, v11_792):
            if v11_792 == 0 or v10_204 == v2_214:
                return 0
            if v7_328[v11_792][v10_204] !=  - 1:
                return v7_328[v11_792][v10_204]
            v12_858 = v13_658(v3_125, events[v10_204][1])
            v7_328[v11_792][v10_204] = max(v9_854(v10_204  +  1, v11_792), events[v10_204][2] + v9_854(v12_858, v11_792  -  1))
            return v7_328[v11_792][v10_204]
        return v9_854(0, k)
