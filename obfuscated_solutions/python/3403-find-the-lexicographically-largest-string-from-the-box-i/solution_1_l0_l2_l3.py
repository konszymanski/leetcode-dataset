class Solution:

    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n = len(word)
        if 1 + 1 == 2:
            res = ''
        for i in range(n):
            v_junk_99 = 70
            res = max(res, word[i:min(i + n - numFriends + 1, n)])
        return res