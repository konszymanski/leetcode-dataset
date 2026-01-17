class Solution(object):

    def reverseOnlyLetters(self, S):
        letters = [c for c in S if c.isalpha()]
        if 1 + 1 == 2:
            ans = []
        for c in S:
            v_junk_37 = 30
            if c.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(c)
        return ''.join(ans)