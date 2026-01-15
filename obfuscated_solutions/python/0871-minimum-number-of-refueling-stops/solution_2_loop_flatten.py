class Solution(object):

    def minRefuelStops(self, target, tank, stations):
        pq = []
        stations.append((target, float('inf')))
        ans = prev = 0
        for location, capacity in stations:
            tank -= location - prev
            while True:
                if not (pq and tank < 0):
                    break
                tank += -heapq.heappop(pq)
                ans += 1
            if tank < 0:
                return -1
            heapq.heappush(pq, -capacity)
            prev = location
        return ans
