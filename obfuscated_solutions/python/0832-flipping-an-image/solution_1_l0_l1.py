class Solution(object):
    def flipAndInvertImage(self, A):
        for v1_754 in A:
            for v2_214 in v3_125((len(v1_754)  +  1) / 2):
                v1_754[v2_214], v1_754[~v2_214] = v1_754[~v2_214] ^ 1, v1_754[v2_214] ^ 1
        return A
