class Solution:

    def smallestNumber(self, n: int) -> int:
        v1_754 = 1
        while v1_754 < n:
            v1_754 = v1_754 * 2 + 1
        return v1_754