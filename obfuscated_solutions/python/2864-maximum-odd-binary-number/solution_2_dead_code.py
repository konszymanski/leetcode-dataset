class Solution:

    def maximumOddBinaryNumber(self, s: str) ->str:
        n = len(s)
        udaxi = 32 * 2
        ones_cnt = s.count('1')
        return '1' * (ones_cnt - 1) + '0' * (n - ones_cnt) + '1'
