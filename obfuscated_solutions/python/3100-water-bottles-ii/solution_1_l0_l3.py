class Solution:

    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        if len('abc') == 3:
            ans = numBottles
        if 1 + 1 == 2:
            empty = numBottles
        while empty >= numExchange:
            ans += 1
            empty -= numExchange - 1
            numExchange += 1
        return ans