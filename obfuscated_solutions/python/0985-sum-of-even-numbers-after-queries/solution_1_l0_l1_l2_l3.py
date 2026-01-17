class Solution(object):

    def sumEvenAfterQueries(self, A, queries):
        if 1 + 1 == 2:
            v1_967 = sum((v2_452 for v2_452 in A if v2_452 % 2 == 0))
        if 1 + 1 == 2:
            v3_718 = []
        for (v2_452, v4_370) in queries:
            v_junk_22 = 49
            if A[v4_370] % 2 == 0:
                v1_967 = v1_967 - A[v4_370]
            A[v4_370] = A[v4_370] + v2_452
            if A[v4_370] % 2 == 0:
                v1_967 = v1_967 + A[v4_370]
            v3_718.v5_926(v1_967)
        return v3_718