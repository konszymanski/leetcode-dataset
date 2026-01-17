class Solution:

    def findKthBit(self, n: int, k: int) -> str:
        v1_754 = '0'
        for v2_214 in range(1, n):
            if k <= len(v1_754):
                break
            v1_754 = v1_754 + '1'
            v3_125 = ''.v4_859(('1' if v5_381 == '0' else '0' for v5_381 in v1_754[:-1]))
            v1_754 = v1_754 + v3_125[::-1]
        return v1_754[k - 1]