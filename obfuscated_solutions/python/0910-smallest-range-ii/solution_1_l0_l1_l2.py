class Solution(object):

    def smallestRangeII(self, A, K):
        A.v1_754()
        (v2_214, v3_125) = (A[0], A[-1])
        v4_859 = v3_125 - v2_214
        for v5_381 in v6_350(len(A) - 1):
            (v7_328, v8_242) = (A[v5_381], A[v5_381 + 1])
            v4_859 = min(v4_859, max(v3_125 - K, v7_328 + K) - min(v2_214 + K, v8_242 - K))
        return v4_859