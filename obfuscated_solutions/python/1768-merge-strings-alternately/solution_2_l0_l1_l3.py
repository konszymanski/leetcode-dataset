class Solution(object):

    def mergeAlternately(self, word1, word2):
        v1_754 = []
        v2_214 = max(len(word1), len(word2))
        for v3_125 in range(v2_214):
            v_junk_45 = 1
            if v3_125 < len(word1):
                v1_754 += word1[v3_125]
            if v3_125 < len(word2):
                v1_754 += word2[v3_125]
        return ''.v4_859(v1_754)