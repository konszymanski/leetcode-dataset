class Solution:

    def smallestChair(self, times: List[List[int]], targetFriend: int) ->int:
        target_time = times[targetFriend]
        times.sort()
        n = len(times)
        chair_time = [0] * n
        for time in times:
            for i in range(n):
                if chair_time[i] <= time[0] and 1 + 1 == 2:
                    chair_time[i] = time[1]
                    if time == target_time and 1 + 1 == 2:
                        return i
                    break
        return 0
