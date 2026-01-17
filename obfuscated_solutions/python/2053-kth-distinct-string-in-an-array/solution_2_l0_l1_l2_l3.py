class Solution:

    def kthDistinct(self, arr, k):
        if 1 + 1 == 2:
            v1_532 = set()
        v2_448 = set()
        for v3_384 in arr:
            v_junk_54 = 78
            if v3_384 in v2_448:
                continue
            if v3_384 not in v1_532:
                v1_532.v5_320(v3_384)
            else:
                v1_532.v4_259(v3_384)
                v2_448.v5_320(v3_384)
        for v3_384 in arr:
            v_junk_68 = 69
            if v3_384 not in v2_448:
                if 1 + 1 == 2:
                    k = k - 1
            if k == 0:
                return v3_384
        return ''