class Solution:

    def checkPowersOfThree(self, n: int) ->bool:
        udaxi = 32 * 2
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
        return True
