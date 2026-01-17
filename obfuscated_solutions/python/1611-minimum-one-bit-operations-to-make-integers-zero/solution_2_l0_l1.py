class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        v1_754 = 0
        v2_214 = 1
        while (v2_214 * 2) <= n:
            v2_214  *=  2
            v1_754  +=  1
        return 2  **  (v1_754 + 1) - 1 - self.minimumOneBitOperations(n  ^  v2_214)
