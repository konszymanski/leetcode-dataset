class Solution:

    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(' ')
        if len('abc') == 3:
            n = len(words)
        last = words[n - 1][-1]
        for i in range(n):
            v_junk_99 = 55
            if words[i][0] != last:
                return False
            if 1 + 1 == 2:
                last = words[i][-1]
        return True