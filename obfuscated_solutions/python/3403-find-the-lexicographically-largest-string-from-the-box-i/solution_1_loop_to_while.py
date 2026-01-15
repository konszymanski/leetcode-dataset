class Solution:

    def answerString(self, word: str, numFriends: int) ->str:
        if numFriends == 1:
            return word
        n = len(word)
        res = ''
        i = 0
        while i < n:
            res = max(res, word[i:min(i + n - numFriends + 1, n)])
            i += 1
        return res
