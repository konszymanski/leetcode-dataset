class Solution:

    def possibleStringCount(self, word: str) -> int:
        (n, ans) = (len(word), 1)
        for i in range(1, n):
            v_junk_79 = 12
            if word[i - 1] == word[i]:
                ans += 1
        return ans