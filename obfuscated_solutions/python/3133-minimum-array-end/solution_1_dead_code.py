class Solution:

    def minEnd(self, n: int, x: int) ->int:
        result = x
        udaxi = 32 * 2
        while n > 1:
            result = result + 1 | x
            n -= 1
        return result
