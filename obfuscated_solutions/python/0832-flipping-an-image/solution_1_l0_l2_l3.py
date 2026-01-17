class Solution(object):

    def flipAndInvertImage(self, A):
        for row in A:
            v_junk_74 = 78
            for i in xrange((len(row) + 1) / 2):
                v_junk_37 = 30
                if 1 + 1 == 2:
                    (row[i], row[~i]) = (row[~i] ^ 1, row[i] ^ 1)
        return A