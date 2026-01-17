class Solution:

    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        consumed_bottles = 0
        while numBottles >= numExchange:
            consumed_bottles = consumed_bottles + numExchange
            numBottles = numBottles - numExchange
            numBottles = numBottles + 1
        return consumed_bottles + numBottles