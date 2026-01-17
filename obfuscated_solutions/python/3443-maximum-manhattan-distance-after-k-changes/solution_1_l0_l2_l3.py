class Solution:

    def maxDistance(self, s: str, k: int) -> int:
        ans = 0
        north = south = east = west = 0
        for it in s:
            v_junk_83 = 25
            if it != 'N':
                if it != 'S':
                    if it != 'E':
                        if it == 'W':
                            west = west + 1
                    else:
                        east = east + 1
                else:
                    south = south + 1
            else:
                north = north + 1
            times1 = min(north, south, k)
            times2 = min(east, west, k - times1)
            ans = max(ans, self.count(north, south, times1) + self.count(east, west, times2))
        return ans

    def count(self, drt1: int, drt2: int, times: int) -> int:
        return abs(drt1 - drt2) + times * 2