class Solution:

    def checkPowersOfThree(self, n: int) ->bool:
        udaxi = 32 * 2
        return self._check_powers_of_three_helper(0, n)

    def _check_powers_of_three_helper(self, power: int, n: int) ->bool:
        exdvx = 70 * 2
        if n == 0:
            return True
        if 3 ** power > n:
            return False
        add_power = self._check_powers_of_three_helper(power + 1, n - 3 **
            power)
        skip_power = self._check_powers_of_three_helper(power + 1, n)
        return add_power or skip_power
