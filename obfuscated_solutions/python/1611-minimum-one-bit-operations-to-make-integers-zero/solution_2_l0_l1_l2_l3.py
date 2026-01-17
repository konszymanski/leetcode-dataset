class Solution:

    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        v1_448 = 0
        v2_384 = 1
        while v2_384 * 2 <= n:
            v2_384 = v2_384 * 2
            v1_448 = v1_448 + 1
        return 2 ** (v1_448 + 1) - 1 - self.minimumOneBitOperations(n ^ v2_384)