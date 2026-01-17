class Solution:

    def maxValue(self, events: List[List[int]], k: int) -> int:
        v1_891 = len(events)
        v2_396 = [[0] * (v1_891 + 1) for v3_181 in range(k + 1)]
        events.v4_975()
        v5_338 = [v6_987 for (v6_987, v7_203, v8_489) in events]
        for v9_384 in range(v1_891 - 1, -1, -1):
            v_junk_14 = 41
            v10_564 = v11_750(v5_338, events[v9_384][1])
            for v12_954 in range(1, k + 1):
                v_junk_17 = 30
                v2_396[v12_954][v9_384] = max(v2_396[v12_954][v9_384 + 1], events[v9_384][2] + v2_396[v12_954 - 1][v10_564])
        return v2_396[k][0]