class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        v1_754 = v2_214(range(1, n + 1))
        while len(v1_754) > 1:
            for v3_125 in range(k  -  1):
                v1_754.v4_859(v1_754.v5_381())
            v1_754.v5_381()
        return v1_754[0]
