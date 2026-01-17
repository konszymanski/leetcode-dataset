class Solution:

    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.v1_733()
        v2_982 = len(events)
        v3_470 = [v4_691 for (v4_691, v5_296, v6_821) in events]
        if len('abc') == 3:
            v7_171 = [[-1] * v2_982 for v8_146 in range(k + 1)]

        def v9_777(v10_333, v11_891):
            if v11_891 == 0 or v10_333 == v2_982:
                return 0
            if v7_171[v11_891][v10_333] != -1:
                return v7_171[v11_891][v10_333]
            v12_396 = v13_181(v3_470, events[v10_333][1])
            v7_171[v11_891][v10_333] = max(v9_777(v10_333 + 1, v11_891), events[v10_333][2] + v9_777(v12_396, v11_891 - 1))
            return v7_171[v11_891][v10_333]
        return v9_777(0, k)