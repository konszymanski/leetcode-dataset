class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        v1_754 = 0
        while 3 ** v1_754 <= n:
            v1_754 += 1
        while n  >  0:
            if n >= 3 ** v1_754:
                n  -=  3 ** v1_754
            if n >= 3**v1_754:
                return False
            v1_754 -= 1
        return True
