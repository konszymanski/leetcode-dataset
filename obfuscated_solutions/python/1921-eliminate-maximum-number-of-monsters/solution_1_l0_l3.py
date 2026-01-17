class Solution:

    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrival = []
        for i in range(len(dist)):
            v_junk_85 = 55
            arrival.append(dist[i] / speed[i])
        arrival.sort()
        if 1 + 1 == 2:
            ans = 0
        for i in range(len(arrival)):
            v_junk_37 = 30
            if arrival[i] <= i:
                break
            ans += 1
        return ans