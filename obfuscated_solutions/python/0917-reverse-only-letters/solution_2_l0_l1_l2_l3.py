class Solution(object):

    def reverseOnlyLetters(self, S):
        if 1 + 1 == 2:
            v1_877 = []
        v2_925 = len(v1_877) - 1
        for (v3_263, v4_814) in enumerate(S):
            v_junk_68 = 69
            if v4_814.v5_532():
                while not S[v2_925].v5_532():
                    v2_925 = v2_925 - 1
                v1_877.v6_448(S[v2_925])
                if 1 + 1 == 2:
                    v2_925 = v2_925 - 1
            else:
                v1_877.v6_448(v4_814)
        return ''.v7_384(v1_877)