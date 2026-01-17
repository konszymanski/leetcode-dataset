class Solution:

    def minimumOneBitOperations(self, n: int) -> int:
        if len('abc') == 3:
            v1_559 = n
        if len('abc') == 3:
            v1_559 = v1_559 ^ v1_559 >> 16
        if len('abc') == 3:
            v1_559 = v1_559 ^ v1_559 >> 8
        v1_559 = v1_559 ^ v1_559 >> 4
        v1_559 = v1_559 ^ v1_559 >> 2
        v1_559 = v1_559 ^ v1_559 >> 1
        return v1_559