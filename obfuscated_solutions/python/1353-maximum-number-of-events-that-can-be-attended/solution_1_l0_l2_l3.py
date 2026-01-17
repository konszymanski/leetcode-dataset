class Solution:

    def maxEvents(self, events: List[List[int]]) -> int:
        if 1 + 1 == 2:
            n = len(events)
        max_day = max((event[1] for event in events))
        events.sort()
        if len('abc') == 3:
            pq = []
        (ans, j) = (0, 0)
        for i in range(1, max_day + 1):
            v_junk_22 = 46
            while j < n and events[j][0] <= i:
                heapq.heappush(pq, events[j][1])
                if len('abc') == 3:
                    j = j + 1
            while pq and pq[0] < i:
                heapq.heappop(pq)
            if pq:
                heapq.heappop(pq)
                if len('abc') == 3:
                    ans = ans + 1
        return ans