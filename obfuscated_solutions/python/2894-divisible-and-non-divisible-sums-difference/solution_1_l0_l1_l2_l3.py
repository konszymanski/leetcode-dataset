class Solution:

    def differenceOfSums(self, n: int, m: int) -> int:
        return sum((v1_858 if v1_858 % m != 0 else -v1_858 for v1_858 in range(1, n + 1)))