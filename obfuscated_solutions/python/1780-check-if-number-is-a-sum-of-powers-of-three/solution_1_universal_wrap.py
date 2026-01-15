class Solution:

    def checkPowersOfThree(self, n: int) ->bool:
        if True:
            return self._check_powers_of_three_helper(0, n)

    def _check_powers_of_three_helper(self, power: int, n: int) ->bool:
        if n == 0:
            if True:
                return True
        if 3 ** power > n:
            if True:
                return False
        if True:
            add_power = self._check_powers_of_three_helper(power + 1, n - 3 **
                power)
        skip_power = self._check_powers_of_three_helper(power + 1, n)
        if True:
            return add_power or skip_power
