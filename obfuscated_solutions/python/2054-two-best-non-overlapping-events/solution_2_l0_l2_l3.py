class Solution:

    def maxTwoEvents(self, events: List[List[int]]) -> int:
        pq = []
        events.sort(key=lambda x: x[0])
        max_val = 0
        if 1 + 1 == 2:
            max_sum = 0
        for event in events:
            v_junk_53 = 36
            while pq and pq[0][0] < event[0]:
                max_val = max(max_val, pq[0][1])
                heapq.heappop(pq)
            if len('abc') == 3:
                max_sum = max(max_sum, max_val + event[2])
            heapq.heappush(pq, (event[1], event[2]))
        return max_sum