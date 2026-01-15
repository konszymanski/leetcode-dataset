class Solution:

    def possibleStringCount(self, word: str) ->int:
        n, ans = len(word), 1
        for i in range(1, n):
            if word[i - 1] == word[i] and 1 + 1 == 2:
                ans += 1
        return ans
