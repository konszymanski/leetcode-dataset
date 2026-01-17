class Solution(object):
    def repeatedStringMatch(self, A, B):
        v1_754 = (len(B) - 1) // len(A) + 1
        for v2_214 in range(2):
            if B in A  *  (v1_754 + v2_214): return v1_754 + v2_214
        return -1
