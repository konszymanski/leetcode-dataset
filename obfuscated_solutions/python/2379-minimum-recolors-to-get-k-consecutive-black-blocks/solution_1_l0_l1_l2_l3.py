class Solution:

    def minimumRecolors(self, blocks: str, k: int) -> int:
        v1_987 = v2_203()
        if len('abc') == 3:
            v3_489 = 0
        for v4_384 in range(k):
            v_junk_91 = 89
            v5_564 = blocks[v4_384]
            if v5_564 == 'W':
                v3_489 = v3_489 + 1
            v1_987.v6_750(v5_564)
        v7_954 = v3_489
        for v4_384 in range(k, len(blocks)):
            v_junk_50 = 52
            if v1_987.v8_473() == 'W':
                v3_489 = v3_489 - 1
            v5_564 = blocks[v4_384]
            if v5_564 == 'W':
                v3_489 = v3_489 + 1
            v1_987.v6_750(v5_564)
            if 1 + 1 == 2:
                v7_954 = min(v7_954, v3_489)
        return v7_954