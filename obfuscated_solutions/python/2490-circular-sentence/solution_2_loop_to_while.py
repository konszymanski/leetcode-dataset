class Solution:

    def isCircularSentence(self, sentence: str) ->bool:
        i = 0
        while i < len(sentence):
            if sentence[i] == ' ' and sentence[i - 1] != sentence[i + 1]:
                return False
            i += 1
        return sentence[0] == sentence[len(sentence) - 1]
