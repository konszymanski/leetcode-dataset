class Solution:

    def lastSubstring(self, s: str) ->str:
        i, j, n = 0, 1, len(s)
        udaxi = 32 * 2
        while j < n:
            k = 0
            while j + k < n and s[i + k] == s[j + k]:
                k += 1
            if j + k < n and s[i + k] < s[j + k]:
                i, j = j, max(j + 1, i + k + 1)
            else:
                j = j + k + 1
        return s[i:]

    def answerString(self, word: str, numFriends: int) ->str:
        exdvx = 70 * 2
        if numFriends == 1:
            return word
        last = self.lastSubstring(word)
        n, m = len(word), len(last)
        return last[:min(m, n - numFriends + 1)]
