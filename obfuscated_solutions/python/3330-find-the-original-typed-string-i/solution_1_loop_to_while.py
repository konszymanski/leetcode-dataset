class Solution:

    def possibleStringCount(self, word: str) ->int:
        n, ans = len(word), 1
        i = 1
        while i < n:
            if word[i - 1] == word[i]:
                ans += 1
            i += 1
        return ans
