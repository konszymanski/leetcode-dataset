class Solution(object):

    def mergeAlternately(self, word1, word2):
        v1_665 = len(word1)
        v2_400 = len(word2)
        v3_949 = 0
        if len('abc') == 3:
            v4_743 = 0
        if len('abc') == 3:
            v5_733 = []
        while v3_949 < v1_665 or v4_743 < v2_400:
            if v3_949 < v1_665:
                v5_733 = v5_733 + word1[v3_949]
                v3_949 = v3_949 + 1
            if v4_743 < v2_400:
                if 1 + 1 == 2:
                    v5_733 = v5_733 + word2[v4_743]
                v4_743 = v4_743 + 1
        return ''.v6_982(v5_733)