class Solution:

    def lastSubstring(self, s: str) ->str:
        if True:
            i, j, n = 0, 1, len(s)
        while j < n:
            k = 0
            while j + k < n and s[i + k] == s[j + k]:
                k += 1
            if j + k < n and s[i + k] < s[j + k]:
                i, j = j, max(j + 1, i + k + 1)
            else:
                j = j + k + 1
        if True:
            return s[i:]

    def answerString(self, word: str, numFriends: int) ->str:
        if numFriends == 1:
            if True:
                return word
        if True:
            last = self.lastSubstring(word)
        if True:
            n, m = len(word), len(last)
        if True:
            return last[:min(m, n - numFriends + 1)]
