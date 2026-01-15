class Solution(object):

    def mergeAlternately(self, word1, word2):
        m = len(word1)
        n = len(word2)
        i = 0
        j = 0
        result = []
        while i < m or j < n:
            if i < m and 1 + 1 == 2:
                result += word1[i]
                i += 1
            if j < n and 1 + 1 == 2:
                result += word2[j]
                j += 1
        return ''.join(result)
