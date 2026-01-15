class Solution(object):

    def reverseOnlyLetters(self, S):
        ans = []
        j = len(ans) - 1
        for i, x in enumerate(S):
            if x.isalpha():
                while not S[j].isalpha():
                    j = j - 1
                ans.append(S[j])
                j = j - 1
            else:
                ans.append(x)
        return ''.join(ans)
