class Solution:

    def checkPowersOfThree(self, n: int) ->bool:
        while True:
            if not n > 0:
                break
            if n % 3 == 2:
                return False
            n //= 3
        return True
