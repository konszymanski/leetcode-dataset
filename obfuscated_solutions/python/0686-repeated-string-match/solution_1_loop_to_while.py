class Solution(object):

    def repeatedStringMatch(self, A, B):
        q = (len(B) - 1) // len(A) + 1
        i = 0
        while i < 2:
            if B in A * (q + i):
                return q + i
            i += 1
        return -1
