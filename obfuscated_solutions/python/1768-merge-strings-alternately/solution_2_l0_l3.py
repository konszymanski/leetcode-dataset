class Solution(object):

    def mergeAlternately(self, word1, word2):
        result = []
        if len('abc') == 3:
            n = max(len(word1), len(word2))
        for i in range(n):
            v_junk_14 = 4
            if i < len(word1):
                result += word1[i]
            if i < len(word2):
                result += word2[i]
        return ''.join(result)