class Solution:

    def minimumRecolors(self, blocks: str, k: int) -> int:
        v1_754 = v2_214()
        v3_125 = 0
        for v4_859 in range(k):
            v5_381 = blocks[v4_859]
            if v5_381 == 'W':
                v3_125 = v3_125 + 1
            v1_754.v6_350(v5_381)
        v7_328 = v3_125
        for v4_859 in range(k, len(blocks)):
            if v1_754.v8_242() == 'W':
                v3_125 = v3_125 - 1
            v5_381 = blocks[v4_859]
            if v5_381 == 'W':
                v3_125 = v3_125 + 1
            v1_754.v6_350(v5_381)
            v7_328 = min(v7_328, v3_125)
        return v7_328