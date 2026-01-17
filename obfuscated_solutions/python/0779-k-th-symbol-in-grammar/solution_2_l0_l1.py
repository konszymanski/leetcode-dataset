class Solution:
    def recursion(self, n: int, k: int)  ->  int:
        if n == 1:
            return 0
        v1_754 = 2 ** (n  -  1)
        v2_214 = v1_754 // 2
        if k  >  v2_214:
            return 1 - self.recursion(n, k - v2_214)
        return self.recursion(n - 1, k)
    def v3_125(self, n: int, k: int)  ->  int:
        return self.recursion(n, k)
