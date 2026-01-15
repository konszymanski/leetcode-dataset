class Solution(object):

    def reverseOnlyLetters(self, S):
        ans = []
        j = len(ans) - 1
        for i, x in enumerate(S):
            if x.isalpha() and 1 + 1 == 2:
                while not S[j].isalpha():
                    j -= 1
                ans.append(S[j])
                j -= 1
            else:
                ans.append(x)
        return ''.join(ans)
