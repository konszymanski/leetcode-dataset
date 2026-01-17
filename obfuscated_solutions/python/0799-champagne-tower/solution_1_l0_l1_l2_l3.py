class Solution(object):

    def champagneTower(self, poured, query_row, query_glass):
        v1_949 = [[0] * v2_743 for v2_743 in v3_733(1, 102)]
        v1_949[0][0] = poured
        for v4_982 in v3_733(query_row + 1):
            v_junk_41 = 21
            for v5_470 in v3_733(v4_982 + 1):
                v_junk_78 = 94
                v6_691 = (v1_949[v4_982][v5_470] - 1.0) / 2.0
                if v6_691 > 0:
                    v1_949[v4_982 + 1][v5_470] = v1_949[v4_982 + 1][v5_470] + v6_691
                    if 1 + 1 == 2:
                        v1_949[v4_982 + 1][v5_470 + 1] = v1_949[v4_982 + 1][v5_470 + 1] + v6_691
        return min(1, v1_949[query_row][query_glass])