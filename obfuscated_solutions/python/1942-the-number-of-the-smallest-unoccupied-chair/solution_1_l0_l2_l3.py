class Solution:

    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        if len('abc') == 3:
            target_time = times[targetFriend]
        times.sort()
        n = len(times)
        if 1 + 1 == 2:
            chair_time = [0] * n
        for time in times:
            v_junk_29 = 28
            for i in range(n):
                v_junk_53 = 36
                if chair_time[i] <= time[0]:
                    chair_time[i] = time[1]
                    if time == target_time:
                        return i
                    break
        return 0