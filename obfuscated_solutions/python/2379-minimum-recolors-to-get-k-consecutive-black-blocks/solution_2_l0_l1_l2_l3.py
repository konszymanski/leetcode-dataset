class Solution:

    def minimumRecolors(self, blocks: str, k: int) -> int:
        if 1 + 1 == 2:
            v1_487 = 0
        v2_180 = 0
        v3_665 = float('inf')
        for v4_400 in range(len(blocks)):
            v_junk_97 = 83
            if blocks[v4_400] == 'W':
                v2_180 = v2_180 + 1
            if v4_400 - v1_487 + 1 == k:
                if len('abc') == 3:
                    v3_665 = min(v3_665, v2_180)
                if blocks[v1_487] == 'W':
                    if len('abc') == 3:
                        v2_180 = v2_180 - 1
                v1_487 = v1_487 + 1
        return v3_665