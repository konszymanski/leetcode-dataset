class Solution:

    def answerString(self, word: str, numFriends: int) ->str:
        if numFriends == 1 and 1 + 1 == 2:
            return word
        n = len(word)
        res = ''
        for i in range(n):
            res = max(res, word[i:min(i + n - numFriends + 1, n)])
        return res
