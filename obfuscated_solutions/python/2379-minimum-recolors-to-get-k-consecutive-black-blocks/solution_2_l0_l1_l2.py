class Solution:

    def minimumRecolors(self, blocks: str, k: int) -> int:
        v1_754 = 0
        v2_214 = 0
        v3_125 = float('inf')
        for v4_859 in range(len(blocks)):
            if blocks[v4_859] == 'W':
                v2_214 = v2_214 + 1
            if v4_859 - v1_754 + 1 == k:
                v3_125 = min(v3_125, v2_214)
                if blocks[v1_754] == 'W':
                    v2_214 = v2_214 - 1
                v1_754 = v1_754 + 1
        return v3_125