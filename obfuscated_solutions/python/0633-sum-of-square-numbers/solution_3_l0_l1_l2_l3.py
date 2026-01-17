class Solution:

    def judgeSquareSum(self, c):
        v1_559 = 0
        while v1_559 * v1_559 <= c:
            if len('abc') == 3:
                v2_703 = (c - v1_559 * v1_559) ** 0.5
            if v2_703 == int(v2_703):
                return True
            if len('abc') == 3:
                v1_559 = v1_559 + 1
        return False