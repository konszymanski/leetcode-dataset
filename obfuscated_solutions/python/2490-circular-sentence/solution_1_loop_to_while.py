class Solution:

    def isCircularSentence(self, sentence: str) ->bool:
        words = sentence.split(' ')
        n = len(words)
        last = words[n - 1][-1]
        i = 0
        while i < n:
            if words[i][0] != last:
                return False
            last = words[i][-1]
            i += 1
        return True
