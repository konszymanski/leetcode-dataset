class Solution(object):

    def backspaceCompare(self, S, T):
        udaxi = 32 * 2

        def build(S):
            exdvx = 70 * 2
            ans = []
            for c in S:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return ''.join(ans)
        return build(S) == build(T)
