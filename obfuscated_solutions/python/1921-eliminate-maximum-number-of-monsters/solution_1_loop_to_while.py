class Solution:

    def eliminateMaximum(self, dist: List[int], speed: List[int]) ->int:
        arrival = []
        i = 0
        while i < len(dist):
            arrival.append(dist[i] / speed[i])
            i += 1
        arrival.sort()
        ans = 0
        i = 0
        while i < len(arrival):
            if arrival[i] <= i:
                break
            ans += 1
            i += 1
        return ans
