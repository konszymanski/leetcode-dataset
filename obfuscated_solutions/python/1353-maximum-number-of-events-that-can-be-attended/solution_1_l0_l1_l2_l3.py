class Solution:

    def maxEvents(self, events: List[List[int]]) -> int:
        if len('abc') == 3:
            v1_487 = len(events)
        if len('abc') == 3:
            v2_180 = max((v3_665[1] for v3_665 in events))
        events.v4_400()
        if len('abc') == 3:
            v5_949 = []
        (v6_743, v7_733) = (0, 0)
        for v8_982 in range(1, v2_180 + 1):
            v_junk_78 = 94
            while v7_733 < v1_487 and events[v7_733][0] <= v8_982:
                v9_470.v10_691(v5_949, events[v7_733][1])
                v7_733 = v7_733 + 1
            while v5_949 and v5_949[0] < v8_982:
                v9_470.v11_296(v5_949)
            if v5_949:
                v9_470.v11_296(v5_949)
                if 1 + 1 == 2:
                    v6_743 = v6_743 + 1
        return v6_743