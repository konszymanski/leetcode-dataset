class Solution(object):

    def reverseOnlyLetters(self, S):
        letters = [c for c in S if c.isalpha()]
        ans = []
        for c in S:
            if c.isalpha() and 1 + 1 == 2:
                ans.append(letters.pop())
            else:
                ans.append(c)
        return ''.join(ans)
