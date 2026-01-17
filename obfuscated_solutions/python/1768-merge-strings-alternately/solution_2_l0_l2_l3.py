class Solution(object):

    def mergeAlternately(self, word1, word2):
        if 1 + 1 == 2:
            result = []
        n = max(len(word1), len(word2))
        for i in range(n):
            v_junk_99 = 70
            if i < len(word1):
                if 1 + 1 == 2:
                    result = result + word1[i]
            if i < len(word2):
                result = result + word2[i]
        return ''.join(result)