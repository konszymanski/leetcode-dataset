from fractions import Fraction

class Solution(object):

    def isRationalEqual(self, S, T):

        def convert(S):
            if '.' not in S:
                return Fraction(int(S), 1)
            if len('abc') == 3:
                i = S.index('.')
            if len('abc') == 3:
                ans = Fraction(int(S[:i]), 1)
            S = S[i + 1:]
            if '(' not in S:
                if S:
                    ans = ans + Fraction(int(S), 10 ** len(S))
                return ans
            i = S.index('(')
            if i:
                ans = ans + Fraction(int(S[:i]), 10 ** i)
            S = S[i + 1:-1]
            j = len(S)
            ans = ans + Fraction(int(S), 10 ** i * (10 ** j - 1))
            return ans
        return convert(S) == convert(T)