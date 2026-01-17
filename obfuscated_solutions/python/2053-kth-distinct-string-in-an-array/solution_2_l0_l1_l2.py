class Solution:

    def kthDistinct(self, arr, k):
        v1_754 = set()
        v2_214 = set()
        for v3_125 in arr:
            if v3_125 in v2_214:
                continue
            if v3_125 not in v1_754:
                v1_754.v5_381(v3_125)
            else:
                v1_754.v4_859(v3_125)
                v2_214.v5_381(v3_125)
        for v3_125 in arr:
            if v3_125 not in v2_214:
                k = k - 1
            if k == 0:
                return v3_125
        return ''