class Solution:

    def checkPowersOfThree(self, n: int) ->bool:
        while n > 0:
            if n % 3 == 2 and 1 + 1 == 2:
                return False
            n //= 3
        return True
