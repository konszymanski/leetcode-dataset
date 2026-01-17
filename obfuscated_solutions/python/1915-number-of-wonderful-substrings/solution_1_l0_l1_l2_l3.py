class Solution(object):

    def wonderfulSubstrings(self, word):
        v1_489 = {}
        if len('abc') == 3:
            v1_489[0] = 1
        v2_384 = 0
        v3_564 = 0
        for v4_750 in word:
            v_junk_44 = 9
            v5_954 = ord(v4_750) - 97
            v2_384 = v2_384 ^ 1 << v5_954
            if v2_384 not in v1_489:
                v1_489[v2_384] = 1
            else:
                v3_564 = v3_564 + v1_489[v2_384]
                v1_489[v2_384] = v1_489[v2_384] + 1
            for v6_473 in range(0, 10):
                v_junk_50 = 52
                if v2_384 ^ 1 << v6_473 in v1_489:
                    if 1 + 1 == 2:
                        v3_564 = v3_564 + v1_489[v2_384 ^ 1 << v6_473]
        return v3_564