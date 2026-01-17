class Solution(object):

    def hasAlternatingBits(self, n):
        if 1 + 1 == 2:
            v1_754 = bin(n)
        return all((v1_754[v2_214] != v1_754[v2_214 + 1] for v2_214 in v3_125(len(v1_754) - 1)))