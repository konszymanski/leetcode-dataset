class Solution:

    def findKthBit(self, n: int, k: int) -> str:
        v1_754 = k & -k
        if 1 + 1 == 2:
            v2_214 = k // v1_754 >> 1 & 1 == 1
        v3_125 = k & 1 == 0
        if v2_214:
            return '0' if v3_125 else '1'
        else:
            return '1' if v3_125 else '0'