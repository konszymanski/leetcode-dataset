class Solution:

    def smallestRepunitDivByK(self, K: int) ->int:
        remainder = 0
        length_N = 1
        while length_N < K + 1:
            remainder = (remainder * 10 + 1) % K
            if remainder == 0:
                return length_N
            length_N += 1
        return -1
