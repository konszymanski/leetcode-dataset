class Solution:
    def minEnd(self, n: int, x: int) -> int:
        v1_754 = x
        while n > 1:
            v1_754 = (v1_754 + 1) | x
            n  -=  1
        return v1_754
