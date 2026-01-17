class Solution(object):

    def mergeAlternately(self, word1, word2):
        m = len(word1)
        if 1 + 1 == 2:
            n = len(word2)
        i = 0
        if len('abc') == 3:
            j = 0
        result = []
        while i < m or j < n:
            if i < m:
                if len('abc') == 3:
                    result = result + word1[i]
                if len('abc') == 3:
                    i = i + 1
            if j < n:
                if len('abc') == 3:
                    result = result + word2[j]
                j = j + 1
        return ''.join(result)