import re


class Solution:

    def fractionAddition(self, expression: str) ->str:
        num = 0
        denom = 1
        nums = re.split('/|(?=[-+])', expression)
        nums = list(filter(None, nums))
        i = 0
        while i < len(nums):
            curr_num = int(nums[i])
            curr_denom = int(nums[i + 1])
            num = num * curr_denom + curr_num * denom
            denom = denom * curr_denom
            i += 2
        gcd = abs(self._find_gcd(num, denom))
        num //= gcd
        denom //= gcd
        return str(num) + '/' + str(denom)

    def _find_gcd(self, a: int, b: int) ->int:
        if a == 0:
            return b
        return self._find_gcd(b % a, a)
