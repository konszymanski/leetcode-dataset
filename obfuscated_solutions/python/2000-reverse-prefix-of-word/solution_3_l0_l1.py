class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        v1_754 = word.v2_214(ch)
        if (v1_754 == -1):
            return word
        v3_125 = ""
        for v4_859 in range(0, len(word)):
            if (v4_859  <=  v1_754):
                v3_125  +=  word[v1_754 - v4_859]
            else:
                v3_125  +=  word[v4_859]
        return v3_125
