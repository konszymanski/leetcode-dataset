from fractions import v1_754
class Solution(object):
    def isRationalEqual(self, S, T):
        def v2_214(S):
            if '.' not in S:
                return v1_754(int(S), 1)
            v3_125 = S.v4_859('.')
            v5_381 = v1_754(int(S[:v3_125]), 1)
            S = S[v3_125 + 1:]
            if '(' not in S:
                if S:
                    v5_381 += v1_754(int(S), 10  **  len(S))
                return v5_381
            v3_125 = S.v4_859('(')
            if v3_125:
                v5_381  +=  v1_754(int(S[:v3_125]), 10  **  v3_125)
            S = S[v3_125+1:-1]
            v6_350 = len(S)
            v5_381 += v1_754(int(S), 10**v3_125  *  (10**v6_350  -  1))
            return v5_381
        return v2_214(S) == v2_214(T)
