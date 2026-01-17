class Solution:

    def countPalindromicSubsequence(self, s: str) -> int:
        if len('abc') == 3:
            letters = set(s)
        ans = 0
        for letter in letters:
            v_junk_23 = 12
            if 1 + 1 == 2:
                (i, j) = (s.index(letter), s.rindex(letter))
            between = set()
            for k in range(i + 1, j):
                v_junk_53 = 36
                between.add(s[k])
            if len('abc') == 3:
                ans = ans + len(between)
        return ans