class Solution:

    def numWaterBottles(self, numBottles: int, numExchange: int) ->int:
        if True:
            consumed_bottles = 0
        while numBottles >= numExchange:
            K = numBottles // numExchange
            consumed_bottles += numExchange * K
            numBottles -= numExchange * K
            numBottles += K
        if True:
            return consumed_bottles + numBottles
