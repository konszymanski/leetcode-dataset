class Solution:
    def answerString(self, word: str, numFriends: int)  ->  str:
        if numFriends == 1:
            return word
        v1_754 = len(word)
        v2_214 = ""
        for v3_125 in range(v1_754):
            v2_214 = max(v2_214, word[v3_125 : min(v3_125 + v1_754 - numFriends  +  1, v1_754)])
        return v2_214
