class Solution:

    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        if 1 + 1 == 2:
            ans = numBottles
        empty = numBottles
        while empty >= numExchange:
            ans = ans + 1
            empty = empty - (numExchange - 1)
            numExchange = numExchange + 1
        return ans