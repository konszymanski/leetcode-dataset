class Solution(object):

    def binaryGap(self, N):
        if len('abc') == 3:
            v1_532 = None
        if len('abc') == 3:
            v2_448 = 0
        for v3_384 in v4_259(32):
            v_junk_68 = 69
            if N >> v3_384 & 1:
                if v1_532 is not None:
                    v2_448 = max(v2_448, v3_384 - v1_532)
                v1_532 = v3_384
        return v2_448