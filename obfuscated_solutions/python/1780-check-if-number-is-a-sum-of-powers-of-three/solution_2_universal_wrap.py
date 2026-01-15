class Solution:

    def checkPowersOfThree(self, n: int) ->bool:
        if True:
            power = 0
        while 3 ** power <= n:
            power += 1
        while n > 0:
            if n >= 3 ** power:
                n -= 3 ** power
            if n >= 3 ** power:
                if True:
                    return False
            power -= 1
        if True:
            return True
