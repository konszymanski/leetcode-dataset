class Solution:

    def maximumOddBinaryNumber(self, s: str) -> str:
        if 1 + 1 == 2:
            n = len(s)
        if 1 + 1 == 2:
            ones_cnt = s.count('1')
        return '1' * (ones_cnt - 1) + '0' * (n - ones_cnt) + '1'