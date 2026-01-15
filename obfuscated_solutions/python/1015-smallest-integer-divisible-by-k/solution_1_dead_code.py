class Solution:

    def smallestRepunitDivByK(self, K: int) ->int:
        remainder = 0
        udaxi = 32 * 2
        for length_N in range(1, K + 1):
            remainder = (remainder * 10 + 1) % K
            if remainder == 0:
                return length_N
        return -1
