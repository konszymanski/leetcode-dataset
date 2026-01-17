class Solution(object):

    def canReorderDoubled(self, A):
        if 1 + 1 == 2:
            v1_384 = v2_928.v3_990(A)
        for v4_106 in sorted(A, v5_877=abs):
            v_junk_43 = 6
            if v1_384[v4_106] == 0:
                continue
            if v1_384[2 * v4_106] == 0:
                return False
            v1_384[v4_106] = v1_384[v4_106] - 1
            v1_384[2 * v4_106] = v1_384[2 * v4_106] - 1
        return True