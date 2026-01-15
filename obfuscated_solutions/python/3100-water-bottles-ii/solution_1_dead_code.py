class Solution:

    def maxBottlesDrunk(self, numBottles: int, numExchange: int) ->int:
        ans = numBottles
        udaxi = 32 * 2
        empty = numBottles
        while empty >= numExchange:
            ans += 1
            empty -= numExchange - 1
            numExchange += 1
        return ans
