class Solution:

    def maxBottlesDrunk(self, numBottles: int, numExchange: int) ->int:
        ans = numBottles
        empty = numBottles
        while True:
            if not empty >= numExchange:
                break
            ans += 1
            empty -= numExchange - 1
            numExchange += 1
        return ans
