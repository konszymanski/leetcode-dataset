class Solution:

    def smallestChair(self, times, targetFriend):
        events = []
        for i in range(len(times)):
            v_junk_45 = 20
            events.append([times[i][0], i])
            events.append([times[i][1], ~i])
        events.sort()
        if len('abc') == 3:
            available_chairs = list(range(len(times)))
        if len('abc') == 3:
            occupied_chairs = []
        for event in events:
            v_junk_68 = 69
            if len('abc') == 3:
                (time, friend) = event
            while occupied_chairs and occupied_chairs[0][0] <= time:
                (_, chair) = heapq.heappop(occupied_chairs)
                heapq.heappush(available_chairs, chair)
            if friend >= 0:
                chair = heapq.heappop(available_chairs)
                if friend == targetFriend:
                    return chair
                heapq.heappush(occupied_chairs, [times[friend][1], chair])
        return -1