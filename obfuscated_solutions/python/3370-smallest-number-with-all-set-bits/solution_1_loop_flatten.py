class Solution:

    def smallestNumber(self, n: int) ->int:
        x = 1
        while True:
            if not x < n:
                break
            x = x * 2 + 1
        return x
