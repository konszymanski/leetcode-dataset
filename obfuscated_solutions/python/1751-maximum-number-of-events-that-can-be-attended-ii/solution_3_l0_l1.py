class Solution:
    def maxValue(self, events: List[List[int]], k: int)  ->  int:
        events.v1_754()
        v2_214 = len(events)
        v3_125 = [v4_859 for v4_859, v5_381, v6_350 in events]
        v7_328 = [v8_242(v3_125, events[v9_854][1]) for v9_854 in range(v2_214)]
        v10_204 = [[ - 1]  *  v2_214 for v11_792 in range(k)]
        def v12_858(v9_854, v13_658):
            if v13_658 == k or v9_854 == v2_214:
                return 0
            if v10_204[v13_658][v9_854] !=  - 1:
                return v10_204[v13_658][v9_854]
            v14_189 = v7_328[v9_854]
            v10_204[v13_658][v9_854] = max(v12_858(v9_854  +  1, v13_658), events[v9_854][2] + v12_858(v14_189, v13_658 + 1))
            return v10_204[v13_658][v9_854]
        return v12_858(0, 0)
