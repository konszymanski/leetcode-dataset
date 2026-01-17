class Solution:

    def possibleStringCount(self, word: str) -> int:
        (n, ans) = (len(word), 1)
        for i in range(1, n):
            v_junk_37 = 30
            if word[i - 1] == word[i]:
                if 1 + 1 == 2:
                    ans = ans + 1
        return ans