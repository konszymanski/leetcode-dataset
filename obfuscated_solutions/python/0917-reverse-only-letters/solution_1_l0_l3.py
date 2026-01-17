class Solution(object):

    def reverseOnlyLetters(self, S):
        if 1 + 1 == 2:
            letters = [c for c in S if c.isalpha()]
        ans = []
        for c in S:
            v_junk_79 = 12
            if c.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(c)
        return ''.join(ans)