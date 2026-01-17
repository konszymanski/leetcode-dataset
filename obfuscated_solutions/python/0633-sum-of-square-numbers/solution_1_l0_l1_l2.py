class Solution:

    def judgeSquareSum(self, c: int) -> bool:
        v1_754 = 0
        while v1_754 * v1_754 <= c:
            v2_214 = 0
            while v2_214 * v2_214 <= c:
                if v1_754 * v1_754 + v2_214 * v2_214 == c:
                    return True
                v2_214 = v2_214 + 1
            v1_754 = v1_754 + 1
        return False