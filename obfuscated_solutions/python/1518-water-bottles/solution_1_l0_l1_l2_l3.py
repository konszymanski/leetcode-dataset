class Solution:

    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        v1_818 = 0
        while numBottles >= numExchange:
            v1_818 = v1_818 + numExchange
            if len('abc') == 3:
                numBottles = numBottles - numExchange
            if len('abc') == 3:
                numBottles = numBottles + 1
        return v1_818 + numBottles