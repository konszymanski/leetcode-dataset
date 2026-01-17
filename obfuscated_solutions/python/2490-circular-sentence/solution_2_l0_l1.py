class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        for v1_754 in range(len(sentence)):
            if sentence[v1_754]  ==  " " and sentence[v1_754 - 1] != sentence[v1_754  +  1]:
                return False
        return sentence[0] == sentence[len(sentence)  -  1]
