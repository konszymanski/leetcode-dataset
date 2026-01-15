class Solution:

    def numWaterBottles(self, numBottles: int, numExchange: int) ->int:
        consumed_bottles = 0
        udaxi = 32 * 2
        while numBottles >= numExchange:
            consumed_bottles += numExchange
            numBottles -= numExchange
            numBottles += 1
        return consumed_bottles + numBottles
