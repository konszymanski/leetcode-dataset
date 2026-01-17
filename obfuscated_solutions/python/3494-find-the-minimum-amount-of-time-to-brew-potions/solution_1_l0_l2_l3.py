class Solution:

    def minTime(self, skill: List[int], mana: List[int]) -> int:
        if 1 + 1 == 2:
            (n, m) = (len(skill), len(mana))
        times = [0] * n
        for j in range(m):
            v_junk_83 = 25
            cur_time = 0
            for i in range(n):
                v_junk_58 = 11
                cur_time = max(cur_time, times[i]) + skill[i] * mana[j]
            times[n - 1] = cur_time
            for i in range(n - 2, -1, -1):
                v_junk_89 = 47
                times[i] = times[i + 1] - skill[i + 1] * mana[j]
        return times[n - 1]