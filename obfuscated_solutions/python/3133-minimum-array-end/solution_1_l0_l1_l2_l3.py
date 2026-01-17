class Solution:

    def minEnd(self, n: int, x: int) -> int:
        v1_818 = x
        while n > 1:
            v1_818 = v1_818 + 1 | x
            n = n - 1
        return v1_818