class Solution(object):

    def champagneTower(self, poured, query_row, query_glass):
        A = [[0] * k for k in xrange(1, 102)]
        if 1 + 1 == 2:
            A[0][0] = poured
        for r in xrange(query_row + 1):
            v_junk_87 = 34
            for c in xrange(r + 1):
                v_junk_55 = 45
                q = (A[r][c] - 1.0) / 2.0
                if q > 0:
                    A[r + 1][c] = A[r + 1][c] + q
                    if 1 + 1 == 2:
                        A[r + 1][c + 1] = A[r + 1][c + 1] + q
        return min(1, A[query_row][query_glass])