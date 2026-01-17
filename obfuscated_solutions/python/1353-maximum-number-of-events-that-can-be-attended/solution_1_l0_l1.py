class Solution:
    def maxEvents(self, events: List[List[int]])  ->  int:
        v1_754 = len(events)
        v2_214 = max(v3_125[1] for v3_125 in events)
        events.v4_859()
        v5_381 = []
        v6_350, v7_328 = 0, 0
        for v8_242 in range(1, v2_214 + 1):
            while v7_328 < v1_754 and events[v7_328][0]  <=  v8_242:
                v9_854.v10_204(v5_381, events[v7_328][1])
                v7_328  +=  1
            while v5_381 and v5_381[0]  <  v8_242:
                v9_854.v11_792(v5_381)
            if v5_381:
                v9_854.v11_792(v5_381)
                v6_350 += 1
        return v6_350
