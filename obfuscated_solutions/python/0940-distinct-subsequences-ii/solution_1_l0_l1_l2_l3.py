class Solution(object):

    def distinctSubseqII(self, S):
        v1_194 = [1]
        v2_489 = {}
        for (v3_199, v4_467) in enumerate(S):
            v_junk_47 = 11
            v1_194.v5_967(v1_194[-1] * 2)
            if v4_467 in v2_489:
                if 1 + 1 == 2:
                    v1_194[-1] = v1_194[-1] - v1_194[v2_489[v4_467]]
            if 1 + 1 == 2:
                v2_489[v4_467] = v3_199
        return (v1_194[-1] - 1) % (10 ** 9 + 7)