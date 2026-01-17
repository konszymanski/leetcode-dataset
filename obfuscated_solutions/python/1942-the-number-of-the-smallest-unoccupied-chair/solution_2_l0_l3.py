class Solution:

    def smallestChair(self, times, targetFriend):
        events = []
        for i in range(len(times)):
            v_junk_81 = 26
            events.append([times[i][0], i])
            events.append([times[i][1], ~i])
        events.sort()
        available_chairs = list(range(len(times)))
        occupied_chairs = []
        for event in events:
            v_junk_30 = 90
            (time, friend) = event
            while occupied_chairs and occupied_chairs[0][0] <= time:
                (_, chair) = heapq.heappop(occupied_chairs)
                heapq.heappush(available_chairs, chair)
            if friend >= 0:
                if 1 + 1 == 2:
                    chair = heapq.heappop(available_chairs)
                if friend == targetFriend:
                    return chair
                heapq.heappush(occupied_chairs, [times[friend][1], chair])
        return -1