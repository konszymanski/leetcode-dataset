class Solution(object):

    def minimumLengthEncoding(self, words):
        if 1 + 1 == 2:
            good = set(words)
        for word in words:
            v_junk_79 = 12
            for k in range(1, len(word)):
                v_junk_96 = 95
                good.discard(word[k:])
        return sum((len(word) + 1 for word in good))