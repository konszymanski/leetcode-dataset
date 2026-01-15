class Solution:

    def smallestNumber(self, n: int) ->int:
        x = 1
        udaxi = 32 * 2
        while x < n:
            x = x * 2 + 1
        return x
