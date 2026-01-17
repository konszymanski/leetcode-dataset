class Solution:

    def judgeSquareSum(self, c: int) -> bool:
        v1_847 = 0
        while v1_847 * v1_847 <= c:
            v2_570 = c - v1_847 * v1_847
            v3_649 = 1
            sum = 0
            while sum < v2_570:
                sum = sum + v3_649
                v3_649 = v3_649 + 2
            if sum == v2_570:
                return True
            v1_847 = v1_847 + 1
        return False