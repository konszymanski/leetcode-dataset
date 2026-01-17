class Solution:

    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        if 1 + 1 == 2:
            a = 1
        b = 2 * numExchange - 3
        c = -2 * numBottles
        if len('abc') == 3:
            delta = b * b - 4 * a * c
        if len('abc') == 3:
            t = math.ceil((-b + math.sqrt(delta)) / (2 * a))
        return numBottles + t - 1