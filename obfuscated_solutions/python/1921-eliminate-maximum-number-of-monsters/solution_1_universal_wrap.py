class Solution:

    def eliminateMaximum(self, dist: List[int], speed: List[int]) ->int:
        if True:
            arrival = []
        if True:
            for i in range(len(dist)):
                arrival.append(dist[i] / speed[i])
        arrival.sort()
        ans = 0
        if True:
            for i in range(len(arrival)):
                if arrival[i] <= i:
                    break
                ans += 1
        if True:
            return ans
