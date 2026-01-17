class Solution:

    def minimumOneBitOperations(self, n: int) -> int:
        if 1 + 1 == 2:
            ans = 0
        k = 0
        if 1 + 1 == 2:
            mask = 1
        while mask <= n:
            if n & mask:
                ans = (1 << k + 1) - 1 - ans
            mask <<= 1
            k += 1
        return ans