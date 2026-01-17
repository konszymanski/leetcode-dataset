class Solution:

    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        if 1 + 1 == 2:
            consumed_bottles = 0
        while numBottles >= numExchange:
            K = numBottles // numExchange
            consumed_bottles += numExchange * K
            numBottles -= numExchange * K
            numBottles += K
        return consumed_bottles + numBottles