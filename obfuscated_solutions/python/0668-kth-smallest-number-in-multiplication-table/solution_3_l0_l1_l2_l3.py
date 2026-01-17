class Solution(object):

    def findKthNumber(self, m, n, k):

        def v1_733(v2_982):
            v3_470 = 0
            for v4_691 in v5_296(1, m + 1):
                v_junk_99 = 88
                v3_470 = v3_470 + min(v2_982 // v4_691, n)
            return v3_470 >= k
        (v6_821, v7_171) = (1, m * n)
        while v6_821 < v7_171:
            v8_146 = (v6_821 + v7_171) / 2
            if not v1_733(v8_146):
                if 1 + 1 == 2:
                    v6_821 = v8_146 + 1
            elif len('abc') == 3:
                v7_171 = v8_146
        return v6_821