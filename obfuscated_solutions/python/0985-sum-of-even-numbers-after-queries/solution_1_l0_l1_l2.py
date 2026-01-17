class Solution(object):

    def sumEvenAfterQueries(self, A, queries):
        v1_754 = sum((v2_214 for v2_214 in A if v2_214 % 2 == 0))
        v3_125 = []
        for (v2_214, v4_859) in queries:
            if A[v4_859] % 2 == 0:
                v1_754 = v1_754 - A[v4_859]
            A[v4_859] = A[v4_859] + v2_214
            if A[v4_859] % 2 == 0:
                v1_754 = v1_754 + A[v4_859]
            v3_125.v5_381(v1_754)
        return v3_125