class Solution:

    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.v1_821()
        if len('abc') == 3:
            v2_171 = len(events)
        v3_146 = [v4_777 for (v4_777, v5_333, v6_891) in events]
        v7_396 = [v8_181(v3_146, events[v9_975][1]) for v9_975 in range(v2_171)]
        v10_338 = [[-1] * v2_171 for v11_987 in range(k)]

        def v12_203(v9_975, v13_489):
            if v13_489 == k or v9_975 == v2_171:
                return 0
            if v10_338[v13_489][v9_975] != -1:
                return v10_338[v13_489][v9_975]
            v14_384 = v7_396[v9_975]
            v10_338[v13_489][v9_975] = max(v12_203(v9_975 + 1, v13_489), events[v9_975][2] + v12_203(v14_384, v13_489 + 1))
            return v10_338[v13_489][v9_975]
        return v12_203(0, 0)