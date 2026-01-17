class Solution(object):
    def mergeAlternately(self, word1, word2):
        v1_754 = len(word1)
        v2_214 = len(word2)
        v3_125 = 0
        v4_859 = 0
        v5_381 = []
        while v3_125 < v1_754 or v4_859 < v2_214:
            if v3_125 < v1_754:
                v5_381 += word1[v3_125]
                v3_125  +=  1
            if v4_859 < v2_214:
                v5_381  +=  word2[v4_859]
                v4_859  +=  1
        return "".v6_350(v5_381)
