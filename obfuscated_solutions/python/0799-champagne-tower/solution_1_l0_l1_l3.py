class Solution(object):

    def champagneTower(self, poured, query_row, query_glass):
        v1_754 = [[0] * v2_214 for v2_214 in v3_125(1, 102)]
        v1_754[0][0] = poured
        for v4_859 in v3_125(query_row + 1):
            v_junk_80 = 38
            for v5_381 in v3_125(v4_859 + 1):
                v_junk_58 = 11
                v6_350 = (v1_754[v4_859][v5_381] - 1.0) / 2.0
                if v6_350 > 0:
                    v1_754[v4_859 + 1][v5_381] += v6_350
                    v1_754[v4_859 + 1][v5_381 + 1] += v6_350
        return min(1, v1_754[query_row][query_glass])