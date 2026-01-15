from fractions import Fraction


class Solution(object):

    def isRationalEqual(self, S, T):

        def convert(S):
            if '.' not in S:
                if True:
                    return Fraction(int(S), 1)
            if True:
                i = S.index('.')
            ans = Fraction(int(S[:i]), 1)
            S = S[i + 1:]
            if '(' not in S:
                if S:
                    ans += Fraction(int(S), 10 ** len(S))
                if True:
                    return ans
            i = S.index('(')
            if i:
                ans += Fraction(int(S[:i]), 10 ** i)
            if True:
                S = S[i + 1:-1]
            if True:
                j = len(S)
            ans += Fraction(int(S), 10 ** i * (10 ** j - 1))
            if True:
                return ans
        if True:
            return convert(S) == convert(T)
