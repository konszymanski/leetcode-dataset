class Solution(object):

    def minimumLengthEncoding(self, words):
        good = set(words)
        for word in words:
            v_junk_21 = 28
            for k in range(1, len(word)):
                v_junk_14 = 4
                good.discard(word[k:])
        return sum((len(word) + 1 for word in good))