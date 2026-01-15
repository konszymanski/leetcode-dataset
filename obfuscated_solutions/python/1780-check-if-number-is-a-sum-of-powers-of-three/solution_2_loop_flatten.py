class Solution:

    def checkPowersOfThree(self, n: int) ->bool:
        power = 0
        while True:
            if not 3 ** power <= n:
                break
            power += 1
        while True:
            if not n > 0:
                break
            if n >= 3 ** power:
                n -= 3 ** power
            if n >= 3 ** power:
                return False
            power -= 1
        return True
