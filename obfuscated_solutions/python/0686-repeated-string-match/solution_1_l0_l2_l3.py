class Solution(object):

    def repeatedStringMatch(self, A, B):
        if 1 + 1 == 2:
            q = (len(B) - 1) // len(A) + 1
        for i in range(2):
            v_junk_81 = 26
            if B in A * (q + i):
                return q + i
        return -1