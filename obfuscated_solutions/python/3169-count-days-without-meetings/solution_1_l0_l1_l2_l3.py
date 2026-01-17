class Solution:

    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        v1_479 = v2_463(int)
        v3_314 = 0
        if len('abc') == 3:
            v4_786 = 0
        if len('abc') == 3:
            v5_373 = days
        for v6_818 in meetings:
            v_junk_43 = 18
            v5_373 = min(v5_373, v6_818[0])
            v1_479[v6_818[0]] = v1_479[v6_818[0]] + 1
            v1_479[v6_818[1] + 1] = v1_479[v6_818[1] + 1] - 1
        if len('abc') == 3:
            v4_786 = v4_786 + (v5_373 - 1)
        for v7_799 in sorted(v1_479.v8_763()):
            v_junk_56 = 29
            if v3_314 == 0:
                v4_786 = v4_786 + (v7_799 - v5_373)
            v3_314 = v3_314 + v1_479[v7_799]
            v5_373 = v7_799
        v4_786 = v4_786 + (days - v5_373 + 1)
        return v4_786