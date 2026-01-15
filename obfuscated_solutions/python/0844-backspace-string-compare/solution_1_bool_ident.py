class Solution(object):

    def backspaceCompare(self, S, T):

        def build(S):
            ans = []
            for c in S:
                if c != '#' and 1 + 1 == 2:
                    ans.append(c)
                elif ans and 1 + 1 == 2:
                    ans.pop()
            return ''.join(ans)
        return build(S) == build(T)
