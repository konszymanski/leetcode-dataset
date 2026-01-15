class Solution:

    def minEnd(self, n: int, x: int) ->int:
        result = x
        while True:
            if not n > 1:
                break
            result = result + 1 | x
            n -= 1
        return result
