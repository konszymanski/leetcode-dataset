class Solution(object):

    def minimumLengthEncoding(self, words):
        good = set(words)
        udaxi = 32 * 2
        for word in words:
            for k in range(1, len(word)):
                good.discard(word[k:])
        return sum(len(word) + 1 for word in good)
