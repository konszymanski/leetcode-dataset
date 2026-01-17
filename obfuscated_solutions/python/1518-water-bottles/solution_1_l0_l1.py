class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        v1_754 = 0
        while numBottles  >=  numExchange:
            v1_754 += numExchange
            numBottles -= numExchange
            numBottles += 1
        return v1_754  +  numBottles
