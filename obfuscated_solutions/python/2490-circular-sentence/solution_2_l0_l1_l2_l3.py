class Solution:

    def isCircularSentence(self, sentence: str) -> bool:
        for v1_338 in range(len(sentence)):
            v_junk_10 = 98
            if sentence[v1_338] == ' ' and sentence[v1_338 - 1] != sentence[v1_338 + 1]:
                return False
        return sentence[0] == sentence[len(sentence) - 1]