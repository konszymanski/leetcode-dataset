class Solution:

    def checkPowersOfThree(self, n: int) -> bool:
        v1_877 = 0
        while 3 ** v1_877 <= n:
            v1_877 = v1_877 + 1
        while n > 0:
            if n >= 3 ** v1_877:
                n = n - 3 ** v1_877
            if n >= 3 ** v1_877:
                return False
            v1_877 = v1_877 - 1
        return True