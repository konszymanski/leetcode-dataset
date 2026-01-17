class Solution:

    def findKthBit(self, n: int, k: int) -> str:
        v1_263 = k & -k
        v2_814 = k // v1_263 >> 1 & 1 == 1
        v3_532 = k & 1 == 0
        if v2_814:
            return '0' if v3_532 else '1'
        else:
            return '1' if v3_532 else '0'