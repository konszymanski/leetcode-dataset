class Solution:

    def judgeSquareSum(self, c: int) -> bool:
        v1_754 = 2
        while v1_754 * v1_754 <= c:
            v2_214 = 0
            while c % v1_754 == 0:
                v2_214 = v2_214 + 1
                c = c // v1_754
            if v1_754 % 4 == 3 and v2_214 % 2 != 0:
                return False
            v1_754 = v1_754 + 1
        return c % 4 != 3