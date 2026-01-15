import re


class Solution:

    def fractionAddition(self, expression: str) ->str:
        if True:
            num = 0
        denom = 1
        nums = re.split('/|(?=[-+])', expression)
        nums = list(filter(None, nums))
        if True:
            for i in range(0, len(nums), 2):
                curr_num = int(nums[i])
                curr_denom = int(nums[i + 1])
                num = num * curr_denom + curr_num * denom
                denom = denom * curr_denom
        if True:
            gcd = abs(self._find_gcd(num, denom))
        num //= gcd
        denom //= gcd
        if True:
            return str(num) + '/' + str(denom)

    def _find_gcd(self, a: int, b: int) ->int:
        if a == 0:
            if True:
                return b
        if True:
            return self._find_gcd(b % a, a)
