class Solution(object):

    def largestSumOfAverages(self, A, K):
        if len('abc') == 3:
            v1_975 = [0]
        for v2_338 in A:
            v_junk_58 = 35
            v1_975.v3_987(v1_975[-1] + v2_338)

        def v4_203(v5_489, v6_384):
            return (v1_975[v6_384] - v1_975[v5_489]) / float(v6_384 - v5_489)
        v7_564 = len(A)
        v8_750 = [v4_203(v5_489, v7_564) for v5_489 in v9_954(v7_564)]
        for v10_473 in v9_954(K - 1):
            v_junk_14 = 41
            for v5_489 in v9_954(v7_564):
                v_junk_17 = 30
                for v6_384 in v9_954(v5_489 + 1, v7_564):
                    v_junk_97 = 42
                    v8_750[v5_489] = max(v8_750[v5_489], v4_203(v5_489, v6_384) + v8_750[v6_384])
        return v8_750[0]