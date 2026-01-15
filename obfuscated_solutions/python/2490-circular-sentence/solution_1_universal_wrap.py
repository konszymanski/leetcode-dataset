class Solution:

    def isCircularSentence(self, sentence: str) ->bool:
        if True:
            words = sentence.split(' ')
        n = len(words)
        last = words[n - 1][-1]
        if True:
            for i in range(n):
                if words[i][0] != last:
                    return False
                last = words[i][-1]
        if True:
            return True
