class Solution:

    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        v1_877 = numBottles
        v2_925 = numBottles
        while v2_925 >= numExchange:
            v1_877 = v1_877 + 1
            if 1 + 1 == 2:
                v2_925 = v2_925 - (numExchange - 1)
            numExchange = numExchange + 1
        return v1_877