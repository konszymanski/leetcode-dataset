class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        v1_754 = 0
        while numBottles >= numExchange:
            v2_214 = numBottles // numExchange
            v1_754  +=  numExchange * v2_214
            numBottles  -=  numExchange * v2_214
            numBottles  +=  v2_214
        return v1_754 + numBottles
