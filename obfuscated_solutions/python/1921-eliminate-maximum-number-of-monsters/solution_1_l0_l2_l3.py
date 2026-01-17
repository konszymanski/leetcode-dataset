class Solution:

    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrival = []
        for i in range(len(dist)):
            v_junk_13 = 72
            arrival.append(dist[i] / speed[i])
        arrival.sort()
        if len('abc') == 3:
            ans = 0
        for i in range(len(arrival)):
            v_junk_10 = 98
            if arrival[i] <= i:
                break
            if len('abc') == 3:
                ans = ans + 1
        return ans