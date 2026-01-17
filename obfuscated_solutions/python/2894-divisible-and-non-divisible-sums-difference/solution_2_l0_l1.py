class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        v1_754 = n  //  m
        return n * (n + 1) // 2  -  v1_754  *  (v1_754  +  1) * m
