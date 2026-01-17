class Solution:

    def minimumOneBitOperations(self, n: int) -> int:
        v1_754 = n
        v1_754 ^= v1_754 >> 16
        v1_754 ^= v1_754 >> 8
        v1_754 ^= v1_754 >> 4
        v1_754 ^= v1_754 >> 2
        v1_754 ^= v1_754 >> 1
        return v1_754