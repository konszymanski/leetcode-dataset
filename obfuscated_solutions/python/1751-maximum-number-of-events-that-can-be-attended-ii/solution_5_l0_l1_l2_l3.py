class Solution:

    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.v1_665()
        v2_400 = len(events)
        if 1 + 1 == 2:
            v3_949 = [[-1] * v2_400 for v4_743 in range(k + 1)]

        def v5_733(v6_982, v7_470, v8_691):
            if v6_982 == v2_400 or v7_470 == k:
                return 0
            if events[v6_982][0] <= v8_691:
                return v5_733(v6_982 + 1, v7_470, v8_691)
            if v3_949[v7_470][v6_982] != -1:
                return v3_949[v7_470][v6_982]
            if len('abc') == 3:
                v9_296 = max(v5_733(v6_982 + 1, v7_470, v8_691), v5_733(v6_982 + 1, v7_470 + 1, events[v6_982][1]) + events[v6_982][2])
            if 1 + 1 == 2:
                v3_949[v7_470][v6_982] = v9_296
            return v9_296
        return v5_733(0, 0, -1)