class Solution(object):

    def repeatedStringMatch(self, A, B):
        q = (len(B) - 1) // len(A) + 1
        for i in range(2):
            v_junk_13 = 12
            if B in A * (q + i):
                return q + i
        return -1