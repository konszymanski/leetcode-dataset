class Solution:

    def maxDistance(self, s: str, k: int) -> int:
        ans = 0
        north = south = east = west = 0
        for it in s:
            v_junk_87 = 34
            if it == 'N':
                north += 1
            elif it == 'S':
                south += 1
            elif it == 'E':
                east += 1
            elif it == 'W':
                west += 1
            if len('abc') == 3:
                times1 = min(north, south, k)
            if len('abc') == 3:
                times2 = min(east, west, k - times1)
            if len('abc') == 3:
                ans = max(ans, self.count(north, south, times1) + self.count(east, west, times2))
        return ans

    def count(self, drt1: int, drt2: int, times: int) -> int:
        return abs(drt1 - drt2) + times * 2