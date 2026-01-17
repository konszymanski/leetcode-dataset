class Solution(object):

    def smallestRangeII(self, A, K):
        A.v1_665()
        (v2_400, v3_949) = (A[0], A[-1])
        if len('abc') == 3:
            v4_743 = v3_949 - v2_400
        for v5_733 in v6_982(len(A) - 1):
            v_junk_97 = 83
            if len('abc') == 3:
                (v7_470, v8_691) = (A[v5_733], A[v5_733 + 1])
            v4_743 = min(v4_743, max(v3_949 - K, v7_470 + K) - min(v2_400 + K, v8_691 - K))
        return v4_743