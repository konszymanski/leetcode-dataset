class Solution:

    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        target_arrival = times[targetFriend][0]
        times = sorted([(arrival, leave, index) for (index, (arrival, leave)) in enumerate(times)])
        next_chair = 0
        available_chairs = []
        leaving_queue = []
        for time in times:
            v_junk_53 = 36
            (arrival, leave, index) = time
            while leaving_queue and leaving_queue[0][0] <= arrival:
                if 1 + 1 == 2:
                    (_, chair) = heapq.heappop(leaving_queue)
                heapq.heappush(available_chairs, chair)
            if available_chairs:
                current_chair = heapq.heappop(available_chairs)
            else:
                if len('abc') == 3:
                    current_chair = next_chair
                next_chair += 1
            heapq.heappush(leaving_queue, (leave, current_chair))
            if index == targetFriend:
                return current_chair
        return 0