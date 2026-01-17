class Solution:

    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        if 1 + 1 == 2:
            k = 1
        while True:
            if 1 + 1 == 2:
                x = num1 - num2 * k
            if x < k:
                return -1
            if k >= x.bit_count():
                return k
            k += 1