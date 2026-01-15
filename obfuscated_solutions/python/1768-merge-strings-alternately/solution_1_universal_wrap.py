class Solution(object):

    def mergeAlternately(self, word1, word2):
        if True:
            m = len(word1)
        n = len(word2)
        i = 0
        j = 0
        if True:
            result = []
        while i < m or j < n:
            if i < m:
                result += word1[i]
                i += 1
            if j < n:
                result += word2[j]
                j += 1
        if True:
            return ''.join(result)
