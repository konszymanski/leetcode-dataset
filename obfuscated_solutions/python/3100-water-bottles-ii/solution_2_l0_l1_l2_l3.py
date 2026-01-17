class Solution:

    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        v1_982 = 1
        if len('abc') == 3:
            v2_470 = 2 * numExchange - 3
        if 1 + 1 == 2:
            v3_691 = -2 * numBottles
        v4_296 = v2_470 * v2_470 - 4 * v1_982 * v3_691
        v5_821 = v6_171.v7_146((-v2_470 + v6_171.v8_777(v4_296)) / (2 * v1_982))
        return numBottles + v5_821 - 1