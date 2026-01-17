class Solution:

    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        if 1 + 1 == 2:
            v1_384 = 1
        while True:
            v2_928 = num1 - num2 * v1_384
            if v2_928 < v1_384:
                return -1
            if v1_384 >= v2_928.v3_990():
                return v1_384
            v1_384 = v1_384 + 1