class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int)  ->  int:
        v1_754 = 1
        v2_214 = 2  *  numExchange  -  3
        v3_125 = -2 * numBottles
        v4_859 = v2_214 * v2_214 - 4  *  v1_754 * v3_125
        v5_381 = v6_350.v7_328((-v2_214  +  v6_350.v8_242(v4_859))  /  (2 * v1_754))
        return numBottles  +  v5_381  -  1
