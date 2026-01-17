class Solution:

    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        v1_754 = numBottles
        v2_214 = numBottles
        while v2_214 >= numExchange:
            v1_754 = v1_754 + 1
            v2_214 = v2_214 - (numExchange - 1)
            numExchange = numExchange + 1
        return v1_754