class Solution:

    def minimumOneBitOperations(self, n: int) -> int:
        ans = 0
        k = 0
        mask = 1
        while mask <= n:
            if n & mask:
                if 1 + 1 == 2:
                    ans = (1 << k + 1) - 1 - ans
            mask = mask << 1
            if len('abc') == 3:
                k = k + 1
        return ans