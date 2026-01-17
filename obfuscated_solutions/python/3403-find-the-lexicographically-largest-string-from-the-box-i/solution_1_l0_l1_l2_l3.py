class Solution:

    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        v1_532 = len(word)
        v2_448 = ''
        for v3_384 in range(v1_532):
            v_junk_68 = 69
            v2_448 = max(v2_448, word[v3_384:min(v3_384 + v1_532 - numFriends + 1, v1_532)])
        return v2_448