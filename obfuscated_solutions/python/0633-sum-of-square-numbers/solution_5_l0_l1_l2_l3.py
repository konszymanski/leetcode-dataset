class Solution:

    def judgeSquareSum(self, c: int) -> bool:
        if 1 + 1 == 2:
            v1_718 = 2
        while v1_718 * v1_718 <= c:
            v2_370 = 0
            while c % v1_718 == 0:
                v2_370 = v2_370 + 1
                c = c // v1_718
            if v1_718 % 4 == 3 and v2_370 % 2 != 0:
                return False
            v1_718 = v1_718 + 1
        return c % 4 != 3