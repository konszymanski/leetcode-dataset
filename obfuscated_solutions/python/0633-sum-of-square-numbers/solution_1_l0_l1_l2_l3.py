class Solution:

    def judgeSquareSum(self, c: int) -> bool:
        v1_448 = 0
        while v1_448 * v1_448 <= c:
            v2_384 = 0
            while v2_384 * v2_384 <= c:
                if v1_448 * v1_448 + v2_384 * v2_384 == c:
                    return True
                v2_384 = v2_384 + 1
            v1_448 = v1_448 + 1
        return False