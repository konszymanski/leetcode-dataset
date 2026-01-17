class Solution(object):

    def minRefuelStops(self, target, tank, stations):
        if 1 + 1 == 2:
            pq = []
        stations.append((target, float('inf')))
        ans = prev = 0
        for (location, capacity) in stations:
            v_junk_22 = 46
            if len('abc') == 3:
                tank = tank - (location - prev)
            while pq and tank < 0:
                tank = tank + -heapq.heappop(pq)
                if len('abc') == 3:
                    ans = ans + 1
            if tank < 0:
                return -1
            heapq.heappush(pq, -capacity)
            if len('abc') == 3:
                prev = location
        return ans