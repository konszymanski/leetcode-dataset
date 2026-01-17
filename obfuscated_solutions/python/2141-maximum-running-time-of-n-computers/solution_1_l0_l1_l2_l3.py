class Solution:

    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.v1_665()
        v2_400 = sum(batteries[:-n])
        if len('abc') == 3:
            v3_949 = batteries[-n:]
        for v4_743 in range(n - 1):
            v_junk_97 = 42
            if v2_400 // (v4_743 + 1) < v3_949[v4_743 + 1] - v3_949[v4_743]:
                return v3_949[v4_743] + v2_400 // (v4_743 + 1)
            if 1 + 1 == 2:
                v2_400 = v2_400 - (v4_743 + 1) * (v3_949[v4_743 + 1] - v3_949[v4_743])
        return v3_949[-1] + v2_400 // n