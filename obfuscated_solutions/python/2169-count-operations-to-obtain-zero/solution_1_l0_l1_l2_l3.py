class Solution:

    def countOperations(self, num1: int, num2: int) -> int:
        v1_559 = 0
        while num1 and num2:
            v1_559 = v1_559 + num1 // num2
            if len('abc') == 3:
                num1 = num1 % num2
            if len('abc') == 3:
                (num1, num2) = (num2, num1)
        return v1_559