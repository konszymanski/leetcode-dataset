class Solution:

    def countOperations(self, num1: int, num2: int) -> int:
        v1_754 = 0
        while num1 and num2:
            v1_754 = v1_754 + num1 // num2
            num1 = num1 % num2
            (num1, num2) = (num2, num1)
        return v1_754