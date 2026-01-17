class Solution(object):

    def reverseOnlyLetters(self, S):
        if 1 + 1 == 2:
            ans = []
        j = len(ans) - 1
        for (i, x) in enumerate(S):
            v_junk_99 = 70
            if x.isalpha():
                while not S[j].isalpha():
                    if 1 + 1 == 2:
                        j = j - 1
                ans.append(S[j])
                j = j - 1
            else:
                ans.append(x)
        return ''.join(ans)