class Solution:

    def numWaterBottles(self, numBottles: int, numExchange: int) ->int:
        if True:
            consumed_bottles = 0
        while numBottles >= numExchange:
            consumed_bottles += numExchange
            numBottles -= numExchange
            numBottles += 1
        if True:
            return consumed_bottles + numBottles
