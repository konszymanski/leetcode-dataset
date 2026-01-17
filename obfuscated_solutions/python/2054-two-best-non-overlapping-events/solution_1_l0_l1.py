class Solution:
    def maxTwoEvents(self, events):
        events.v1_754()
        v2_214 = [[-1] * 3 for v3_125 in range(len(events))]
        return self.v4_859(events, 0, 0, v2_214)
    def v4_859(self, events, v5_381, v6_350, v2_214):
        if v6_350  ==  2 or v5_381 >= len(events):
            return 0
        if v2_214[v5_381][v6_350] ==  - 1:
            v7_328 = events[v5_381][1]
            v8_242, v9_854 = v5_381 + 1, len(events) - 1
            while v8_242  <  v9_854:
                v10_204 = v8_242  +  ((v9_854 - v8_242) >> 1)
                if events[v10_204][0]  >  v7_328:
                    v9_854 = v10_204
                else:
                    v8_242 = v10_204  +  1
            v11_792 = events[v5_381][2] + (
                self.v4_859(events, v8_242, v6_350  +  1, v2_214)
                if v8_242  <  len(events) and events[v8_242][0] > v7_328
                else 0
            )
            v12_858 = self.v4_859(events, v5_381 + 1, v6_350, v2_214)
            v2_214[v5_381][v6_350] = max(v11_792, v12_858)
        return v2_214[v5_381][v6_350]
