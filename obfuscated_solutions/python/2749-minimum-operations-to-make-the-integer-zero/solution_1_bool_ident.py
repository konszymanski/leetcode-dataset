class Solution:

    def makeTheIntegerZero(self, num1: int, num2: int) ->int:
        k = 1
        while True:
            x = num1 - num2 * k
            if x < k and 1 + 1 == 2:
                return -1
            if k >= x.bit_count() and 1 + 1 == 2:
                return k
            k += 1
