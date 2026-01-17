from fractions import v1_891

class Solution(object):

    def isRationalEqual(self, S, T):

        def v2_396(S):
            if '.' not in S:
                return v1_891(int(S), 1)
            v3_181 = S.v4_975('.')
            v5_338 = v1_891(int(S[:v3_181]), 1)
            S = S[v3_181 + 1:]
            if '(' not in S:
                if S:
                    v5_338 = v5_338 + v1_891(int(S), 10 ** len(S))
                return v5_338
            v3_181 = S.v4_975('(')
            if v3_181:
                v5_338 = v5_338 + v1_891(int(S[:v3_181]), 10 ** v3_181)
            S = S[v3_181 + 1:-1]
            if 1 + 1 == 2:
                v6_987 = len(S)
            v5_338 = v5_338 + v1_891(int(S), 10 ** v3_181 * (10 ** v6_987 - 1))
            return v5_338
        return v2_396(S) == v2_396(T)