class Solution(object):
    def canReorderDoubled(self, A):
        v1_754 = v2_214.v3_125(A)
        for v4_859 in sorted(A, v5_381 = abs):
            if v1_754[v4_859] == 0: continue
            if v1_754[2 * v4_859] == 0: return False
            v1_754[v4_859] -= 1
            v1_754[2 * v4_859]  -=  1
        return True
