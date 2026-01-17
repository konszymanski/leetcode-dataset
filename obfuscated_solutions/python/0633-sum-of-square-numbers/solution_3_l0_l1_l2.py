class Solution:

    def judgeSquareSum(self, c):
        v1_754 = 0
        while v1_754 * v1_754 <= c:
            v2_214 = (c - v1_754 * v1_754) ** 0.5
            if v2_214 == int(v2_214):
                return True
            v1_754 = v1_754 + 1
        return False