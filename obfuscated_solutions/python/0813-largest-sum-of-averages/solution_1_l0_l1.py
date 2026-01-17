class Solution(object):
    def largestSumOfAverages(self, A, K):
        v1_754 = [0]
        for v2_214 in A: v1_754.v3_125(v1_754[ - 1]  +  v2_214)
        def v4_859(v5_381, v6_350):
            return (v1_754[v6_350] - v1_754[v5_381]) / float(v6_350 - v5_381)
        v7_328 = len(A)
        v8_242 = [v4_859(v5_381, v7_328) for v5_381 in v9_854(v7_328)]
        for v10_204 in v9_854(K-1):
            for v5_381 in v9_854(v7_328):
                for v6_350 in v9_854(v5_381 + 1, v7_328):
                    v8_242[v5_381] = max(v8_242[v5_381], v4_859(v5_381, v6_350) + v8_242[v6_350])
        return v8_242[0]
