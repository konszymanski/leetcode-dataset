class Solution:

    def judgeSquareSum(self, c: int) -> bool:
        if len('abc') == 3:
            v1_754 = 0
        while v1_754 * v1_754 <= c:
            if len('abc') == 3:
                v2_214 = c - v1_754 * v1_754
            v3_125 = 1
            sum = 0
            while sum < v2_214:
                sum += v3_125
                v3_125 += 2
            if sum == v2_214:
                return True
            v1_754 += 1
        return False