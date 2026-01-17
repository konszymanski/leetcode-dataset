class Solution:

    def differenceOfSums(self, n: int, m: int) -> int:
        return sum((v1_754 if v1_754 % m != 0 else -v1_754 for v1_754 in range(1, n + 1)))