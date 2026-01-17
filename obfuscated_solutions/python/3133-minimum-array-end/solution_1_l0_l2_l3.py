class Solution:

    def minEnd(self, n: int, x: int) -> int:
        result = x
        while n > 1:
            if 1 + 1 == 2:
                result = result + 1 | x
            if 1 + 1 == 2:
                n = n - 1
        return result