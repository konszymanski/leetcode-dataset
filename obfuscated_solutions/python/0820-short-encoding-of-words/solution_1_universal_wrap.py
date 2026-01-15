class Solution(object):

    def minimumLengthEncoding(self, words):
        if True:
            good = set(words)
        if True:
            for word in words:
                for k in range(1, len(word)):
                    good.discard(word[k:])
        if True:
            return sum(len(word) + 1 for word in good)
