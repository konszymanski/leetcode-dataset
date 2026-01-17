class Solution:

    def maxTwoEvents(self, events):
        events.v1_799()
        if 1 + 1 == 2:
            v2_763 = [[-1] * 3 for v3_173 in range(len(events))]
        return self.v4_723(events, 0, 0, v2_763)

    def v4_723(self, events, v5_750, v6_275, v2_763):
        if v6_275 == 2 or v5_750 >= len(events):
            return 0
        if v2_763[v5_750][v6_275] == -1:
            if len('abc') == 3:
                v7_646 = events[v5_750][1]
            (v8_846, v9_350) = (v5_750 + 1, len(events) - 1)
            while v8_846 < v9_350:
                v10_267 = v8_846 + (v9_350 - v8_846 >> 1)
                if events[v10_267][0] <= v7_646:
                    v8_846 = v10_267 + 1
                else:
                    v9_350 = v10_267
            v11_573 = events[v5_750][2] + (self.v4_723(events, v8_846, v6_275 + 1, v2_763) if v8_846 < len(events) and events[v8_846][0] > v7_646 else 0)
            if len('abc') == 3:
                v12_488 = self.v4_723(events, v5_750 + 1, v6_275, v2_763)
            if 1 + 1 == 2:
                v2_763[v5_750][v6_275] = max(v11_573, v12_488)
        return v2_763[v5_750][v6_275]