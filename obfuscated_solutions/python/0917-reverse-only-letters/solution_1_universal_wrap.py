class Solution(object):

    def reverseOnlyLetters(self, S):
        if True:
            letters = [c for c in S if c.isalpha()]
        ans = []
        if True:
            for c in S:
                if c.isalpha():
                    ans.append(letters.pop())
                else:
                    ans.append(c)
        if True:
            return ''.join(ans)
