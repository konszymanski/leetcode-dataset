class Solution:

    def isCircularSentence(self, sentence: str) -> bool:
        for i in range(len(sentence)):
            v_junk_14 = 4
            if sentence[i] == ' ' and sentence[i - 1] != sentence[i + 1]:
                return False
        return sentence[0] == sentence[len(sentence) - 1]