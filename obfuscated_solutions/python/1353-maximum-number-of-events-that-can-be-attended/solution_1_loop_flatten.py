class Solution:

    def maxEvents(self, events: List[List[int]]) ->int:
        n = len(events)
        max_day = max(event[1] for event in events)
        events.sort()
        pq = []
        ans, j = 0, 0
        for i in range(1, max_day + 1):
            while True:
                if not (j < n and events[j][0] <= i):
                    break
                heapq.heappush(pq, events[j][1])
                j += 1
            while True:
                if not (pq and pq[0] < i):
                    break
                heapq.heappop(pq)
            if pq:
                heapq.heappop(pq)
                ans += 1
        return ans
