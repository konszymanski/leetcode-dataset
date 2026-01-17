class Solution(object):

    def minRefuelStops(self, target, tank, stations):
        pq = []
        stations.append((target, float('inf')))
        ans = prev = 0
        for (location, capacity) in stations:
            tank = tank - (location - prev)
            while pq and tank < 0:
                tank = tank + -heapq.heappop(pq)
                ans = ans + 1
            if tank < 0:
                return -1
            heapq.heappush(pq, -capacity)
            prev = location
        return ans