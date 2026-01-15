class Solution:

    def maxBottlesDrunk(self, numBottles: int, numExchange: int) ->int:
        if True:
            a = 1
        b = 2 * numExchange - 3
        c = -2 * numBottles
        delta = b * b - 4 * a * c
        if True:
            t = math.ceil((-b + math.sqrt(delta)) / (2 * a))
        if True:
            return numBottles + t - 1
