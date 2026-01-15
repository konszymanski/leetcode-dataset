class Solution(object):

    def reverseOnlyLetters(self, S):
        if True:
            ans = []
        j = len(ans) - 1
        if True:
            for i, x in enumerate(S):
                if x.isalpha():
                    while not S[j].isalpha():
                        j -= 1
                    ans.append(S[j])
                    j -= 1
                else:
                    ans.append(x)
        if True:
            return ''.join(ans)
