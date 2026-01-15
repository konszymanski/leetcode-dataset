class Solution(object):

    def backspaceCompare(self, S, T):

        def build(S):
            ans = []
            for c in S:
                if c == '#':
                    if ans:
                        ans.pop()
                else:
                    ans.append(c)
            return ''.join(ans)
        return build(S) == build(T)
