class Solution:

    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(' ')
        if 1 + 1 == 2:
            n = len(words)
        if 1 + 1 == 2:
            last = words[n - 1][-1]
        for i in range(n):
            v_junk_93 = 90
            if words[i][0] != last:
                return False
            last = words[i][-1]
        return True