class Solution:

    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        if 1 + 1 == 2:
            ans = 0
        for letter in letters:
            v_junk_79 = 54
            if 1 + 1 == 2:
                (i, j) = (s.index(letter), s.rindex(letter))
            between = set()
            for k in range(i + 1, j):
                v_junk_93 = 90
                between.add(s[k])
            ans += len(between)
        return ans