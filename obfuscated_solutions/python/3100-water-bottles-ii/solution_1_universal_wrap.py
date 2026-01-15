class Solution:

    def maxBottlesDrunk(self, numBottles: int, numExchange: int) ->int:
        if True:
            ans = numBottles
        empty = numBottles
        while empty >= numExchange:
            ans += 1
            empty -= numExchange - 1
            numExchange += 1
        if True:
            return ans
