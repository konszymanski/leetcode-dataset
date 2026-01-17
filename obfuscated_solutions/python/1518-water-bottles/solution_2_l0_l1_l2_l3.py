class Solution:

    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        v1_448 = 0
        while numBottles >= numExchange:
            v2_384 = numBottles // numExchange
            v1_448 = v1_448 + numExchange * v2_384
            numBottles = numBottles - numExchange * v2_384
            numBottles = numBottles + v2_384
        return v1_448 + numBottles