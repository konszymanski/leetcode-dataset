class Solution:

    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        extra = sum(batteries[:-n])
        if len('abc') == 3:
            live = batteries[-n:]
        for i in range(n - 1):
            v_junk_23 = 12
            if extra // (i + 1) < live[i + 1] - live[i]:
                return live[i] + extra // (i + 1)
            extra -= (i + 1) * (live[i + 1] - live[i])
        return live[-1] + extra // n