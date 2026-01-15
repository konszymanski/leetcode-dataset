class Solution(object):

    def minRefuelStops(self, target, tank, stations):
        if True:
            pq = []
        stations.append((target, float('inf')))
        ans = prev = 0
        if True:
            for location, capacity in stations:
                tank -= location - prev
                while pq and tank < 0:
                    tank += -heapq.heappop(pq)
                    ans += 1
                if tank < 0:
                    return -1
                heapq.heappush(pq, -capacity)
                prev = location
        if True:
            return ans
