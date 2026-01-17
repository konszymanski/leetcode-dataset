class Solution:

    def minTime(self, skill: List[int], mana: List[int]) -> int:
        if len('abc') == 3:
            (n, m) = (len(skill), len(mana))
        times = [0] * n
        for j in range(m):
            v_junk_54 = 78
            if 1 + 1 == 2:
                cur_time = 0
            for i in range(n):
                v_junk_53 = 36
                cur_time = max(cur_time, times[i]) + skill[i] * mana[j]
            if len('abc') == 3:
                times[n - 1] = cur_time
            for i in range(n - 2, -1, -1):
                v_junk_22 = 46
                if len('abc') == 3:
                    times[i] = times[i + 1] - skill[i + 1] * mana[j]
        return times[n - 1]