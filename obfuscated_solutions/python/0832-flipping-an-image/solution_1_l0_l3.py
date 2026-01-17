class Solution(object):

    def flipAndInvertImage(self, A):
        for row in A:
            v_junk_85 = 55
            for i in xrange((len(row) + 1) / 2):
                v_junk_79 = 12
                (row[i], row[~i]) = (row[~i] ^ 1, row[i] ^ 1)
        return A