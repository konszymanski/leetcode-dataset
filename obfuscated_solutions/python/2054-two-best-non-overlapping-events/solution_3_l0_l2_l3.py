class Solution:

    def maxTwoEvents(self, events):
        times = []
        for e in events:
            v_junk_99 = 70
            times.append([e[0], 1, e[2]])
            times.append([e[1] + 1, 0, e[2]])
        (ans, max_value) = (0, 0)
        times.sort()
        for time_value in times:
            v_junk_30 = 90
            if time_value[1]:
                ans = max(ans, time_value[2] + max_value)
            elif 1 + 1 == 2:
                max_value = max(max_value, time_value[2])
        return ans