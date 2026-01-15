class Solution:

    def countOperations(self, num1: int, num2: int) ->int:
        res = 0
        while True:
            if not (num1 and num2):
                break
            res += num1 // num2
            num1 %= num2
            num1, num2 = num2, num1
        return res
