class Solution:

    def numWaterBottles(self, numBottles: int, numExchange: int) ->int:
        consumed_bottles = 0
        while True:
            if not numBottles >= numExchange:
                break
            consumed_bottles += numExchange
            numBottles -= numExchange
            numBottles += 1
        return consumed_bottles + numBottles
