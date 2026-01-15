class Solution:

    def isCircularSentence(self, sentence: str) ->bool:
        if True:
            for i in range(len(sentence)):
                if sentence[i] == ' ' and sentence[i - 1] != sentence[i + 1]:
                    return False
        if True:
            return sentence[0] == sentence[len(sentence) - 1]
