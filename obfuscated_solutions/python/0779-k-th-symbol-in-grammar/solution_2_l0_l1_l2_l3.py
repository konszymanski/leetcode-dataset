class Solution:

    def recursion(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        v1_384 = 2 ** (n - 1)
        v2_928 = v1_384 // 2
        if k > v2_928:
            return 1 - self.recursion(n, k - v2_928)
        return self.recursion(n - 1, k)

    def v3_990(self, n: int, k: int) -> int:
        return self.recursion(n, k)